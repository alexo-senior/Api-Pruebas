import requests
import mysql.connector
import json



"""print("Requests version:", requests.__version__)

response = requests.get('https://api.github.com')
print("response status code:", response.status_code)"""

url_dragon_1 = 'https://dragonball-api.com/api/planets'
#url_dragon_2 = 'https://dragonball-api.com/api/characters'
#url_dragon_3 = 'https://dragonball-api.com/api/characters?page=2&limit=5'

# Paso 1: Consumir la API
#response = requests.geturl_dragon_2)
response = requests.get(url_dragon_1)

# Verificar el código de estado
if response.status_code == 200:
    print("Contenido de la respuesta:", response.text)  # Imprime el contenido
    
    try:
        data = response.json()
        print(json.dumps(data, indent=4))# Decodificar la respuesta JSON
    except ValueError as e:
        print("Error al decodificar JSON:", e)
        exit()
else:
    print(f"Error: {response.status_code}, {response.text}")
    # Salir si hay un error

# Paso 2: Conectarse a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",        # Reemplaza con tu usuario
    password="root",        # Reemplaza con tu contraseña
    database="dragonball" # Reemplaza con tu base de datos
)

cursor = db.cursor()
exit()
