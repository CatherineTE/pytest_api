import requests
from endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):


    def post(self, payload):
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload)
        self.response_json = self.response.json()

    def check_name(self, name):
        assert self.response_json['name'] == name
