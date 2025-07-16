import requests
import json
import pprint
import mysql.connector



def obtener_personajes():
    #url = 'https://dragonball-api.com/api/characters?page=2&limit=21'
    url = 'https://dragonball-api.com/api/planets'
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error ala conectar con la API: {response.status_code}")
        
        return[]
    
    try:
        data = response.json()
        return data.get('items', [])
    
    except ValueError as e:
        print(f"Error al hacer la decodificacion de  JSON: {e}")
        return[]
    
    #conectar a la base de datos
    conexion = None
def conectar_db():
    try:
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",             
        password="root",         
        database="dragonball"   
)

        print("conexion exitosa")
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar con mysql:{err}")
        exit()
        return None
        
        
def insertar_personajes(characters, conexion):
    cursor = conexion.cursor()
    for character in characters:
        name = character.get('name')
        planets = character.get('planets')
        
    #inserta los datos en una tabla llamada characters
        
        query = """
            INSERT INTO characters (name, planets)
            VALUES (%s, %s)
            """
        #query = """
        #INSERT INTO planets (name, planets)
        #VALUES (%s, %s)
        #"""
        valores = (name , planets)
        
        try:
            cursor.execute(query, valores)
            conexion.commit()
            print("valores insertados correctamente")
        except mysql.connector.Error as err:
            print(f"Error insertando {name}: {err}")
            
            
            
        
    cursor.close()
    conexion.close()
    print("Conexión cerrada")

if __name__ == "__main__":
    
    character = obtener_personajes()
    if character:
        conexion = conectar_db()
        if conexion:
            insertar_personajes(character, conexion)
        
        
        
        
        
        
        

    
    