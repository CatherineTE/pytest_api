import pytest
import requests
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject

@pytest.fixture
def obj_id():
    create_object = CreateObject()
    payload = {
      "name": "Apple MacBook Pro 17",
      "data": {
         "year": 2019,
         "price": 2099.99,
         "CPU model": "Intel Core i9",
         "Hard disk size": "1 TB"
      }
   }
    create_object.post(payload)
    yield create_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_by_id(f'https://api.restful-api.dev/objects/{create_object.response_json['id']}')

