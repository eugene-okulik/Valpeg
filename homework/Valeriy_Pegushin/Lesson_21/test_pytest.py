import requests
import pytest
import allure


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
@allure.step("Начало тестирования")
def hello():
    print('Start testing')
    yield
    print('Testing completed')


@allure.title("Проверка получения созданного объекта по ID")
@allure.feature("Работа с объектами")
@allure.story("Получение объекта")
def test_one_posts(new_post_id, hello):
    with allure.step(f"Отправка GET запроса для объекта ID: {new_post_id}"):
        response = requests.get(
            f'http://objapi.course.qa-practice.com/object/{new_post_id}'
        ).json()
    with allure.step("Проверка соответствия ID в ответе"):
        assert response['id'] == new_post_id


@pytest.mark.parametrize(
    "color, size, obj_id, name",
    [
        ('red', 'big', 11170, 'First new object'),
        ('blue', 'medium', 11171, 'Second new object'),
        ('green', 'small', 11172, 'Third new object')
    ]
)
@allure.title("Создание объекта с параметрами")
@allure.feature("Работа с объектами")
@allure.story("Создание объекта")
def test_post_a_post(color, size, obj_id, name):
    with allure.step("Инициализация теста"):
        print('before test')
    with allure.step("Подготовка тестовых данных"):
        test_data = {
            'data': {
                'color': color,
                'size': size
            },
            'id': obj_id,
            'name': name
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step("Отправка POST запроса для создания объекта"):
        response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=test_data,
        headers=headers
        )
    with allure.step("Проверка успешного создания объекта"):
        assert response.status_code == 200
    with allure.step("Завершение теста"):
        print('after test')


@allure.title("Обновление объекта через PUT запрос")
@allure.feature("Работа с объектами")
@allure.story("Обновление объекта")
def test_put_a_post(new_post_id):
    with allure.step("Подготовка данных для обновления объекта"):
        body = {
            'data': {
                'color': 'yellow',
                'size': 'very big'
            },
            'id': new_post_id,
            'name': 'Second new object'
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step("Отправка PUT запроса для обновления объекта"):
        response = requests.put(
            f'http://objapi.course.qa-practice.com/object/{new_post_id}',
            json=body,
            headers=headers
        )
        response_json = response.json()
    with allure.step("Проверка обновленного имени объекта"):
        assert response_json['name'] == 'Second new object'


@allure.title("Обновление объекта через PATCH запрос")
@allure.feature("Работа с объектами")
@allure.story("Обновление объекта")
def test_patch_a_post(new_post_id):
    with allure.step("Подготовка данных для частичного обновления"):
        body = {
            'data': {
                'color': 'green',
                'size': 'very big'
            },
            'name': 'Third new object'
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step("Отправка PATCH запроса для обновления объекта"):
        response = requests.patch(
            f'http://objapi.course.qa-practice.com/object/{new_post_id}',
            json=body,
            headers=headers
        )
    response_json = response.json()
    with allure.step("Проверка обновленного имени объекта"):
        assert response_json['name'] == 'Third new object'


@allure.title("Удаление объекта через DELETE запрос")
@allure.feature("Работа с объектами")
@allure.story("Удаление объекта")
def test_delete_a_post(new_post_id):
    with allure.step(f"Отправка DELETE запроса для объекта ID: {new_post_id}"):
        response = requests.delete(
            f'http://objapi.course.qa-practice.com/object/{new_post_id}'
        )
    with allure.step("Проверка успешного удаления объекта"):
        assert response.status_code == 200
