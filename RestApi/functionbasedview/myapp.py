import requests
import json

URL="http://127.0.0.1:9494/regstudent/"
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    #converts the python data like dictionary , list etc 
    # data into json string beacuse the get method required the data in json format
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data,headers={"Content-Type": "application/json"})
    #here json() converts the json encoded data into the python datastructure like dictonary ,list etc.
    data=r.json()
    print(data)

#it calls the get_data function which gets the data.
get_data(1)

def post_data():
    data = {
        'name':'rohit',
        'roll':11,
        'city':'ranchi'
    }
    #converts the python data like dictionary , list etc 
    # data into json string beacuse the get method required the data in json format
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data,headers={"Content-Type": "application/json"})
    #here json() converts the json encoded data into the python datastructure like dictonary ,list etc.
    data=r.json()
    print(data)

#it calls the post_data function which post the data.
#post_data()


def update_data():
    data = {
        'id':1,
        'name':'soham',
    }
    #converts the python data like dictionary , list etc 
    # data into json string beacuse the get method required the data in json format
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data,headers={"Content-Type": "application/json"})
    #here json() converts the json encoded data into the python datastructure like dictonary ,list etc.
    data=r.json()
    print(data)

#it call to update_data function for updating the data
#update_data()

def delete_data():
    data = {
        'id':1,
    }
    #converts the python data like dictionary , list etc 
    # data into json string beacuse the get method required the data in json format
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data,headers={"Content-Type": "application/json"})
    #here json() converts the json encoded data into the python datastructure like dictonary ,list etc.
    data=r.json()
    print(data)

#method used to delete the data of an unique id record.
#delete_data()

