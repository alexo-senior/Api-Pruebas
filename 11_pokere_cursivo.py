import requests
import json
import pprint


def get_pokemons(url='http://pokeapi.co/api/v2/pokemon-form/', offset=0):
    args = {'offset':offset} if offset else {}
    
    response = requests.get(url, params=args)
    if response.status_code == 200:
        carga_datos = response.json()
        
        results = carga_datos.get('results', [])
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


    
        
        
                
                
                
    