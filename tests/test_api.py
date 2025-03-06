import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from tests.test_data import payloads


@pytest.mark.parametrize('payload', payloads.create_payloads)
def test_create_object(payload):
    new_create_object = CreateObject()
    new_create_object.post(payload=payload)
    new_create_object.check_response_is_200()
    new_create_object.check_name(payload['name'])


def test_get_object(obj_id):
    get_object = GetObject()
    print(get_object.get_by_id(obj_id))
    get_object.check_response_is_200()
    get_object.check_response_id(obj_id)

@pytest.mark.parametrize('payload', payloads.update_payloads)
def test_update_object(obj_id, payload):
    update_object = UpdateObject()
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
