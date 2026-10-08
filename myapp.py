import requests
import json

URL = 'http://127.0.0.1:8000/studentapi/'

#Function for GET Mehtod
def get_data(id=None): #Read/GET data FROM DB ---> 'GET' Method
    data={}

    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r =requests.get(url = URL, data=json_data)
    data = r.json()
    print(data)

get_data(1)