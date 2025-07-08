import requests
import json
import pprint

if  __name__ == '__main__':
    url = 'https://wallpapercave.com/wp/hQuSTGC.jpg'
    #realiza la peticion sin descargar el contenido con la conexion abierta
    response = requests.get(url, stream=True)
    #descargar la imagen
    with open('paisaje.jpg', 'wb') as file:
        #el metodo iter_content toma el contenido de la imagen y lo dedscarga
        for wallpaper in response.iter_content(1024):
        #guarda el archivo cualquiera que sea, siempre que tenga la extension
        #jpg y que la url termine en  esta extension
            if wallpaper:
                file.write(wallpaper)
    #cierra la conexion
    response.close()
    