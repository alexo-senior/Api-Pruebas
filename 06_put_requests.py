import requests
import json
import pprint



if __name__ == '__main__':
    # Es la dirección a la que se enviará la petición PUT
    url = 'http://httpbin.org/put'
    # Diccionario con los datos que se envían
    payloads = {'nombre': 'Daniel', 'curso': 'python', 'nivel': 'intermedio', 'framework': 'FastApi'}
    # Cabeceras correctas
    headers = {'Content-Type': 'application/json', 'access-token': '123456789'}
    
    # Se envía la petición PUT con los datos en formato JSON y las cabeceras
    response = requests.put(url, data=json.dumps(payloads), headers=headers)
    
    # Se imprime la URL a la que se hizo la petición
    print(response.url)
    
    # Si la respuesta es exitosa, se imprime el nombre del servidor
    if response.status_code == 200:
        headers_response = response.headers
        server = headers_response.get('server', 'No especificado')
        pprint.pprint(server)
        
        
"""Petición PUT

Se envía una petición HTTP de tipo PUT a la URL, con los datos convertidos a JSON y las cabeceras especificadas.
El método PUT se usa para actualizar o reemplazar información en el servidor.
Impresión de la URL

Se imprime la URL a la que se hizo la petición.
Verificación de respuesta

Si la respuesta es exitosa (status_code == 200):
Se obtienen las cabeceras de la respuesta.
Se extrae el nombre del servidor (server).
Se imprime el nombre del servidor usando pprin
EN RESUMEN:
Este codigo envia datos a un servidor usando el metodo put , imprime la url de
la peticion y, si la repsuesta es correcta muestra el nombre del servidor que 
respondio."""