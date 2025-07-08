import requests
import pprint
import json

"""para ver los encabezados headers, ver el content-type, ademas del access-token:123..."""

if __name__ == "__main__":
    
    url = "http://httpbin.org/post"
    payload = {'nombre':'Alexis', 'Curso':'Python','nivel':'intermedio'}
    headers = {'Content-Type': 'application/json', 'access-token':'123456789'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
        
    pprint.pprint(response.url)
    if response.status_code == 200:
        #pprint.pprint(response.content)
        headers_response = response.headers
        server = headers_response['Server']
        pprint.pprint(server)
        #muestra el servidor y la url
        #'http://httpbin.org/post'
        #'gunicorn/19.9.0'
    
