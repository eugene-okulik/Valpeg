import requests
import pytest


@pytest.fixture()
def new_post_id():
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
    post_id = response.json()['id']
    print(post_id)
    yield post_id
    print('after test')
    requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')


@pytest.fixture(scope='session')
def hello():
    print('Start testing')
    yield
    print('Testing completed')


def test_one_posts(new_post_id, hello):
    response = requests.get(
        f'http://objapi.course.qa-practice.com/object/{new_post_id}'
    ).json()
    assert response['id'] == new_post_id


@pytest.mark.parametrize(
    "color, size, obj_id, name",
    [
        ('red', 'big', 11170, 'First new object'),
        ('blue', 'medium', 11171, 'Second new object'),
        ('green', 'small', 11172, 'Third new object')
    ]
)
def test_post_a_post(color, size, obj_id, name):
    print('before test')
    test_data = {
        'data': {
            'color': color,
            'size': size
        },
        'id': obj_id,
        'name': name
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=test_data,
        headers=headers
    )
    assert response.status_code == 200
    print('after test')


def test_put_a_post(new_post_id):
    body = {
        'data': {
            'color': 'yellow',
            'size': 'very big'
        },
        'id': new_post_id,
        'name': 'Second new object'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_post_id}',
        json=body,
        headers=headers
    )
    response_json = response.json()
    assert response_json['name'] == 'Second new object'


def test_patch_a_post(new_post_id):
    body = {
        'data': {
            'color': 'green',
            'size': 'very big'
        },
        'name': 'Third new object'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_post_id}',
        json=body,
        headers=headers
    )
    response_json = response.json()
    assert response_json['name'] == 'Third new object'


def test_delete_a_post(new_post_id):
    response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{new_post_id}'
    )
    assert response.status_code == 200
