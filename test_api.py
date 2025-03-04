import requests

from endpoints.create_object import CreateObject


def test_create_object():
    new_create_object = CreateObject()
    payload = {
      "name": "Apple MacBook Pro 17",
      "data": {
         "year": 2019,
         "price": 2099.99,
         "CPU model": "Intel Core i9",
         "Hard disk size": "1 TB"
      }
    }
    new_create_object.post(payload=payload)
    new_create_object.check_response_is_200()
    new_create_object.check_name(payload['name'])



def test_get_object(obj_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}').json()
    assert response['id'] == obj_id


def test_update_object(obj_id):
    payload = {
        "name": "Apple MacBook Pro 18",
        "data": {
            "year": 2025,
            "price": 2099.99,
            "CPU model": "M10",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
    response_json = response.json()
    assert response_json['name'] == payload['name']
    assert response.status_code == 200

def test_delete_object(obj_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 200
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 404
