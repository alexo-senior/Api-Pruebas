import requests
import mysql.connector
import json

#Conexión a la API de Dragon Ball
#url_dragonball = 'https://dragonball-api.com/api/planets'
#url_dragonball = 'https://dragonball-api.com/api/characters'
url_dragonball = 'https://dragonball-api.com/api/characters?page=2&limit=21'

response = requests.get(url_dragonball)

if response.status_code != 200:
    print(f"Error al conectar  con la API de Dragon Ball: {response.status_code}")
print("conexion exitosa con la api de dragonball")

try:
    data = response.json()
    
    print("Estructura del JSON:")
    
    
    
    print(json.dumps(data, indent=4))
    
except ValueError as e:
    
    print(" Error al decodificar JSON:", e)
    exit()
        

    #Imprimir resumen de datos
    print(" Mostrando los personajes:")
    
    #ciclo for para recorrer los personajes
    
    for characters in data['items'][:20]:
        print(f" Nombre: {characters.get('name')}")
    #imprime la longuitud de los personajes
        
    print(f"los personajes recibidos fueron:{len(data['items'])}")
        
    #en caso de querer mostar todos los personajes:
    """for characters in characters:
        print(f" Nombre: {characters.get('name')}, planets: {characters.get('planets')}")"""
    #Conexión a MySQL
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="dragonball"
        )
        cursor = db.cursor()
        
        print("✅ Conexión a MySQL exitosa")

    except mysql.connector.Error as err:
        print(f" Error al conectar a MySQL: {err}")
        exit()

else:
    print(f"Error: {response.status_code}, {response.text}")
    exit()

        
    



        


    
        
    
    

