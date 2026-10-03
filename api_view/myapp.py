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

get_data()

# Function for POST METHOD
def post_data(): #POST/STORE OR SAVE data IN DB ---> 'POST' Method
    data = {
        'name':"ravi",
        'roll':104,
        'city':'Shivane'
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r =requests.post(url = URL, data=json_data,headers=headers)
    data = r.json()
    print(data)

post_data()

def update_data(): #UPDATE data IN DB ---> 'PUT' Method for complete update and 'PATCH' method for partial update 
    data = {
        'id':3,
        'name':"Sanket",
        'city':'Bhor'
    }

    json_data = json.dumps(data)
    r =requests.put(url = URL, data=json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():# DELETE data IN DB ---> 'PUT' Method
    data = {'id':3}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data = json_data)
    data = r.json()
    print(data)

# delete_data()