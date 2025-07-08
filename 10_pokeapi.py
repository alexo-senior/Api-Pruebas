import requests
import json
import pprint

if __name__ == '__main__':
    url = 'http://pokeapi.co/api/v2/pokemon-form/'
    response = requests.get(url)
    
    if response.status_code == 200:
        #si la respuesta es ok carga los datos en forma de json
        carga_datos = response.json()
        #obtenemos los datos con get y si no me arroja una lista  vacia
        results = carga_datos.get('results', [])
        #existen mas de 1500 pokemons sin embargo se puede mostrar de a 20 en 20
        #iteramos con un for para ver los nombres de los pokemon uno por uno 
        if results: # sila respuesta es ok 
            #recorre la lista en results
            for pokemon in results:
                #el nombre de cada pokemon damelo en una lista de name
                name = pokemon['name']
                
                print(name)
                
        
        