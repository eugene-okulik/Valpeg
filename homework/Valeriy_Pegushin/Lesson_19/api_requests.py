import requests


def one_posts():
    # response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
    response = requests.get('http://objapi.course.qa-practice.com/object/1').json()
    print(response)


def post_a_post():
    body = {
        'data': {'color': 'red', 'size': 'big'},
        'id': 11170,
        'name': 'First new object'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    ).json()
    print(response)


def put_a_post():
    body = {
        'data': {'color': 'yellow', 'size': 'very big'},
        'id': 11170,
        'name': 'Second new object'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        'http://objapi.course.qa-practice.com/object/11170',
        json=body,
        headers=headers
    ).json()
    print(response)


def patch_a_post():
    body = {
        'data': {'color': 'green', 'size': 'very big'},
        'name': 'Third new object'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        'http://objapi.course.qa-practice.com/object/11170',
        json=body,
        headers=headers
    ).json()
    print(response)


def delete_a_post():
    response = requests.delete('http://objapi.course.qa-practice.com/object/11170')
    print(response.status_code)


one_posts()
post_a_post()
put_a_post()
patch_a_post()
delete_a_post()
