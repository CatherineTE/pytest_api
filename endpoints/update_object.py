import requests

class UpdateObject:
    response = None
    response_json = None

    def update_by_id(self, object_id, payload):
        self.response = requests.put(f'https://api.restful-api.dev/objects/{object_id}', json=payload)
        self.response_json = self.response.json()

    def check_response_is_200(self):
        assert self.response.status_code== 200


    def check_response_name(self, name):
        assert self.response_json['name'] == name
