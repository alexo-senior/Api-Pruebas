import requests
import pprint

if __name__ == "__main__":
    
    url = "http://httpbin.org/post"
    payload = {'nombre':'Alexis', 'Curso':'Python','nivel':'intermedio'}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        
        pprint.pprint(response.content)
    else:
        pprint.pprint(f"Error en POST: {response.status_code}")
