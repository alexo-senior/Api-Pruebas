import requests

if __name__ == '__main__':
    #Se crea una lista llamada urls que contiene tres enlaces directos a videos MP4
    urls = [
        'https://videos.pexels.com/video-files/32114960/13691527_1440_2560_60fps.mp4',
        'https://samplelib.com/mp4/sample-5s.mp4',
        'https://filesamples.com/samples/video/mp4/sample_640x360.mp4'
    ]
    #Se usa un ciclo for con enumerate(urls, start=1) para recorrer cada URL y obtener su índice (empezando desde 1)
    for idx, url in enumerate(urls, start=1):
        videos_mp4 = f'video_{idx}.mp4'
        
        #Para cada video, se crea un nombre de archivo único usando el índice, por ejemplo: video_1.mp4, video_2.mp4, etc.
        #Se imprime un mensaje indicando qué archivo se está descargando.
        print(f'Descargando {'video_1.mp4', 'videdo_2.mp4', 'video_3.mp4'}...')
        
        #Se hace una petición HTTP a la URL del video con stream=True para descargarlo por partes.
        
        response = requests.get(url, stream=True)
        
        #Se abre un archivo en modo binario para escribir el contenido descargado.
        
        with open(videos_mp4, 'wb') as file:
            
        #Se recorre el contenido de la respuesta en bloques de 1 MB (1024 * 1024 bytes) y se escribe cada bloque en el archivo.
            for chunk in response.iter_content(1024 * 1024):
                if chunk:
                    file.write(chunk)
                    
        #Se cierra la conexión HTTP con response.close()
        
        response.close()
        
        #Se imprime un mensaje indicando que el archivo se descargó correctamente
        
        print(f'{videos_mp4} descargado correctamente.')
    