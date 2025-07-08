import requests
import json
import pprint

if __name__ == "__main__":
    
    url = "https://rickandmortyapi.com/api/character/3"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        
        content = response.content
        
        #guardar el archiuvo en formato html 
        with open('Ricky.html', 'wb') as file:
            file.write(content)
            
        print("descarga de datos completada")
        
        #si deseo ver el contenido en la terminal uso pprint para ver contenido de la mejor forma
        print(content)
    else:
        print(f"error al dedscargar la pagina:codigo de error{response.status_code}")    
        

        
        #para ver en formato json y trabajar con el valor origin 
        
        #response_json = json.loads(response.text)
        
        #origin = response_json['origin']
        
        #print(f"tu ip es :{origin}")
        
        
"""todos los parametros deben ir en la url, si queremos trabajar con args, se debe generar un nuevo query,
el query se comienza a con un signo ? en el navegador y cada paremtro se va separando con un signo &( amperson),
pero no es la forma mas adecuada, es mejor trajar con un dict, el metodo get se encarga de construir la url"""

        
"""para trabajar con origin se importa el modulo json """ 

#EN EL NAVEGADOR NO SE PUEDEDN HACER PETICIONES POST
#con el metodo post se visualizan mas atributos en la respuesta que con el metodo get 
#en el metodo post los atributos se envian dentrro de data no en la url 
#por eso en la respuesta los datos ya se ven dentro de data y no dentro de args
# si enviamos los parametros con json este mismo se encarga de serializarlos
#si los enviamos con data debemos serializarlos nosotros con data=json,dumps(payloads)




