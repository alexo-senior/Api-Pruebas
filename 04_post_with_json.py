import requests
import json


#Mostrar toda la informacion de forma ordenada en json 
#y de forma bonita en la terminal 

if __name__ == "__main__":
    url = "http://httpbin.org/post"
    payload = {'nombre': 'Alexis', 'Curso': 'Python', 'nivel': 'intermedio'}

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("POST con JSON:")
        data = response.json()
        #Una de las formas de hacerlo:
        #para ver en formato json y trabajar con el valor origin 
        
        #response_json = json.loads(response.text)
        
        #origin = response_json['origin']
        
        #print(f"tu ip es :{origin}")
        print(json.dumps(data, indent=4))  # Para mostrar bonito
        print(f"Tu IP es: {data.get('origin')}")
    else:
        print(f"Error al enviar JSON: {response.status_code}")
        
        
