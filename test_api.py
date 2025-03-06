import requests
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject


payload = {
      "name": "Apple MacBook Pro 17",
      "data": {
         "year": 2019,
         "price": 2099.99,
         "CPU model": "Intel Core i9",
         "Hard disk size": "1 TB"
      }
    }

def test_create_object():
    new_create_object = CreateObject()
    new_create_object.post(payload=payload)
    new_create_object.check_response_is_200()
    new_create_object.check_name(payload['name'])



def test_get_object(obj_id):
    get_object = GetObject()
    get_object.get_by_id(obj_id)
    get_object.check_response_is_200()
    get_object.check_response_id(obj_id)


def test_update_object(obj_id):
    update_object = UpdateObject()
    payload = {
        "name": "Apple MacBook Pro 18",
        "data": {
            "year": 2025,
            "price": 2099.99,
            "CPU model": "M10",
            "Hard disk size": "1 TB"
        }
    }
    update_object.update_by_id(obj_id, payload)
    update_object.check_response_is_200()
    update_object.check_response_name(payload['name'])

def test_delete_object(obj_id):
    delete_object = DeleteObject()
    delete_object.delete_by_id(obj_id)
    delete_object.check_response_is_200()
    get_object = GetObject()
    get_object.get_by_id(obj_id)
    get_object.check_response_is_404()