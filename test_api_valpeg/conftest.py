import pytest
import requests
from endpoints.create_object import CreateObject
from endpoints.complete_object_update import CompleteObjectUpdate
from endpoints.partial_object_update import PartialObjectUpdate
from endpoints.get_object import GetObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def new_object_id():
    print('before test')
    body = {
        'data': {
            'color': 'red',
            'size': 'big'
        },
        'id': 11170,
        'name': 'First new object'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def complete_object_update_endpoint():
    return CompleteObjectUpdate()


@pytest.fixture()
def partial_object_update_endpoint():
    return PartialObjectUpdate()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()
