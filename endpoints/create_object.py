import requests
import pytest

class CreateObject:
    response = None
    response_json = None

    def post(self, payload):
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload)
        self.response_json = self.response.json()

    def check_name(self, name):
        assert self.response_json['name'] == name


    def check_response_is_200(self):
        assert self.response.status_code== 200
