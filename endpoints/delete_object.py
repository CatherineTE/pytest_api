import requests
from endpoints.base_endpoint import BaseEndpoint

class DeleteObject(BaseEndpoint):

    def delete_by_id(self, object_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
        self.response_json = self.response.json()

    def check_response_id(self, id):
        assert self.response_json['id'] == id

    def check_response_is_404(self):
        assert self.response.status_code== 404