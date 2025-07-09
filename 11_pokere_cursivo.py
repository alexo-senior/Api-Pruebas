import requests
import json
import pprint


def get_pokemons(url='http://pokeapi.co/api/v2/pokemon-form/', offset=0):
    
    #me dedvuelve un diccionario con offset, sino me devuelve una lista vacia
    args = {'offset':offset} if offset else {}
    
    response = requests.get(url, params=args)
    #si la respuesta es ok , carga los datos y los convierte a json
    if response.status_code == 200:
        carga_datos = response.json()
        #en la variable results obtenfgo los datos por medio de get
        results = carga_datos.get('results', [])
        #creo un ciclo for para recorrer la lista que me da results y muestra el nombre
        #de cada pókemon
        if results: 
        
            for pokemon in results:
                name = pokemon['name']
                
                print(name)
                
        #imput es lo que el usuario nos va a devolver o escribir        
        next = input("continuar listando? [Y/N]").lower()
        if next == 'y':
            get_pokemons(offset=offset+20)
        
if __name__ == '__main__':
    url = 'http://pokeapi.co/api/v2/pokemon-form/'
    #llama a la funcion
    get_pokemons()
    
    """como se puede observar en la terminal al listar los 20 pokemons, me pregunta que si
    quiero seguir listando con /y/n, en la web se puede hacer esto con el parametro ?offset=20"""


    
        
        
                
                
                
    