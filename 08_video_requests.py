import requests
import json
import pprint

if  __name__ == '__main__':
    #solo que es voideo y debe ser mp4 extension
    url = 'https://videos.pexels.com/video-files/32114960/13691527_1440_2560_60fps.mp4'
    #realiza la peticion sin descargar el contenido con la conexion abierta
    response = requests.get(url, stream=True)
    #descargar la imagen
    with open('video.mp4', 'wb') as file:
        #el metodo iter_content toma el contenido de la imagen y lo dedscarga
        #el tamaño del bloque es mayot para videos 1024*1024
        for video in response.iter_content(1024 * 1024):
        #guarda el archivo cualquiera que sea, siempre que tenga la extension
        #jpg y que la url termine en  esta extension
            if video:
                file.write(video)
    #cierra la conexion
    response.close()