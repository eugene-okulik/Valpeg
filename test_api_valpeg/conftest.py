import pytest
import requests
from endpoints.create_object import CreateObject
from endpoints.complete_object_update import CompleteObjectUpdate
from endpoints.partial_object_update import PartialObjectUpdate
from endpoints.get_object import GetObject
from endpoints.delete_object import DeleteObject
from data import default_body


@pytest.fixture()
def new_object_id(create_object_endpoint, delete_object_endpoint):
    print('before test')
    # Используем метод create_object из класса CreateObject
    create_object_endpoint.create_object(body=default_body)
    # Получаем ID созданного объекта из ответа
    object_id = create_object_endpoint.response.json()['id']
    yield object_id
    # Используем метод delete_object_by_id из класса DeleteObject
    delete_object_endpoint.delete_object_by_id(object_id)


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


@pytest.fixture()
def default_test_data():
    return default_body
