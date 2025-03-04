import pytest
import requests


@pytest.fixture
def obj_id():
    payload = {
      "name": "Apple MacBook Pro 17",
      "data": {
         "year": 2019,
         "price": 2099.99,
         "CPU model": "Intel Core i9",
         "Hard disk size": "1 TB"
      }
   }
    response = requests.post('https://api.restful-api.dev/objects', json = payload).json()
    print(response)
    return response['id']
