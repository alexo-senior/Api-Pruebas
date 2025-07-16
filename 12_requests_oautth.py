import requests
import json
from dotenv import load_dotenv
import os
import http.server
import webbrowser
import threading
import urllib.parse
import socketserver


# === CARGAR VARIABLES DE ENTORNO ===
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
AUTH_URL = os.getenv("AUTH_URL")
TOKEN_URL = os.getenv("TOKEN_URL")
SCOPE = os.getenv("SCOPE")
PORT = int(os.getenv("PORT"))

# === VERIFICAR VARIABLES ===
print("AUTH_URL:", AUTH_URL)
print("REDIRECT_URI:", REDIRECT_URI)
print("CLIENT_ID:", CLIENT_ID)

#  Variable global para capturar el código de autorización 
authorization_code = None

#  Servidor HTTP que captura el código 
class OAuthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global authorization_code
        url = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(url.query)

        if 'code' in params:
            authorization_code = params['code'][0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write("Autenticación exitosa. Puedes volver a tu terminal.".encode('utf-8'))


        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write("Error: No se recibió el código.".encode('utf-8'))

#  Abre el navegador para autorizar 
def open_authorization_url():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
        "response_type": "code"
    }
    url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"
    print("Abriendo navegador para autorización...")
    webbrowser.open(url)

# === Servidor local para escuchar el código ===
def esperar_codigo():
    with socketserver.TCPServer(("localhost", PORT), OAuthHandler) as server:
        server.handle_request()

# === Intercambia código por token ===
def obtener_token(code):
    datos = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI
    }
    headers = {"Accept": "application/json"}
    respuesta = requests.post(TOKEN_URL, data=datos, headers=headers)
    return respuesta.json()

# === Usa el token para obtener datos del usuario ===
def obtener_info_usuario(token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    respuesta = requests.get("https://api.github.com/user", headers=headers)
    return respuesta.json()

# === FLUJO PRINCIPAL ===
if __name__ == "__main__":
    open_authorization_url()

    print(f"Esperando el código de autorización en {REDIRECT_URI} ...")
    thread = threading.Thread(target=esperar_codigo)
    thread.start()
    thread.join()

    if authorization_code:
        print(f"Código recibido: {authorization_code}")
        tokens = obtener_token(authorization_code)
        print("Token recibido:", tokens)

        access_token = tokens.get("access_token")
        if access_token:
            user_info = obtener_info_usuario(access_token)
            print("Información del usuario:")
            print(json.dumps(user_info, indent=2))
        else:
            print("No se recibió el token de acceso.")
    else:
        print("No se recibió el código de autorización.")












