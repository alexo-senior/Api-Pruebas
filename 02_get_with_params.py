import requests 

#MODELO CON PARAMETROS

if __name__ == "__main__":
    url = "http://httpbin.org/get?nombre=Alexis&curso=Python"
    args = {'nombre': 'Alexis', 'curso': 'Python'}

    response = requests.get(url, params=args)

    if response.status_code == 200:
        print("Respuesta con parámetros:")
        print(response.json())
    else:
        print(f"Error en GET con params: {response.status_code}")


