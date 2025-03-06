import requests


class GetObject:
    response = None
    response_json = None

    def get_by_id(self, id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{id}')
        self.response_json = self.response.json()

    def check_response_is_200(self):
        assert self.response.status_code== 200


    def check_response_id(self, object_id):
        assert self.response_json['id'] == object_id

    def check_response_is_404(self):
        assert self.response.status_code== 404