import requests
import json

URL = "http://127.0.0.1:8000/stdapi/"

def get_data(id = None):
    data = {}

    if id is not None :
        data = {'id':id}
    json_data = json.dumps(data)

    r = requests.get(url = URL, data=json_data)

    data = r.json()
    print(data)
#get_data(1)

def post_data():
    data = {
        'id' : 5,
        'Name' : 'Tuhin Pal',
        'Roll' : 3,
        'Address' : '65, Aurora Hills, Kolkata'
        
    }

    json_data = json.dumps(data)

    re = requests.post(url= URL, data = json_data) 
    data = re.json()
    print(data)

#post_data()

def update_data():
    data = {
        'id' : 6,
        'Name' : 'Kiran Kumar Singh',
        'Roll' : 6,
       
        
    }

    json_data = json.dumps(data)

    re = requests.put(url= URL, data = json_data) 
    data = re.json()
    print(data)
    
#update_data()

def delete_data():
    data = {
        'id' : 1,
    }

    json_data = json.dumps(data)

    re = requests.delete(url= URL, data = json_data) 
    data = re.json()
    print(data)
    
delete_data()