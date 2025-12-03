# Импорт необходимых библиотек
import pytest  # Фреймворк для написания тестов

# Данные для позитивных тестов (успешное создание объектов)
TEST_DATA = [
    # Первый набор данных для теста создания объекта
    {'body': {'data': {'color': 'red', 'size': 'big'}, 'name': 'First new object'}},
    # Второй набор данных для теста создания объекта
    {'body': {'data': {'color': 'blue', 'size': 'medium'}, 'name': 'Second new object'}},
    # Третий набор данных для теста создания объекта
    {'body': {'data': {'color': 'green', 'size': 'small'}, 'name': 'Third new object'}}

]

# Данные для негативных тестов (ожидаемые ошибки)
NEGATIVE_TEST_DATA = [
    # Неправильный тип данных для поля 'data' (строка вместо объекта)
    {'body': {'data': 'text', 'name': 'First new object'}},
    # Пустое тело запроса
    {'body': {}},
    # Отсутствует обязательное поле 'name'
    {'body': {'data': {'color': 'red', 'size': 'big'}}},
    # Отсутствует обязательное поле 'data'
    {'body': {'name': 'Test Object'}},
    # Null значения в data
    {'body': {'data': None, 'name': 'Test Object'}},
    # Массив вместо объекта в data
    {'body': {'data': ['red', 'big'], 'name': 'Test Object'}}
]

# Данные для тестов с ошибкой "не найдено" (404)
NOT_FOUND_TEST_DATA = [
    # Неправильный URL endpoint
    {'url': 'http://objapi.course.qa-practice.com/wrong_endpoint',
     'body': {'data': {'color': 'red', 'size': 'big'}, 'name': 'Test Object'}},
    # URL с опечаткой
    {'url': 'http://objapi.course.qa-practice.com/objct',
     'body': {'data': {'color': 'green', 'size': 'small'}, 'name': 'Test Object'}}
]


# Тест получения объекта по ID
def test_get_object(get_object_endpoint, new_object_id):
    # Получаем объект по ID через эндпоинт
    get_object_endpoint.get_object_by_id(new_object_id)
    # Проверяем, что полученный объект имеет правильный ID
    get_object_endpoint.verify_object_id_matches(new_object_id)


# Тест для создания объектов с разными данными
@pytest.mark.parametrize("test_data", TEST_DATA)
def test_create_object(test_data, create_object_endpoint):
    # Извлекаем тело запроса из тестовых данных
    body = test_data['body']
    # Отправляем POST запрос для создания объекта
    create_object_endpoint.create_object(body=body)
    # Проверяем, что объект успешно создан с правильными данными
    create_object_endpoint.verify_object_successfully(
        body['name'],  # Ожидаемое имя объекта
        body['data']['color'],  # Ожидаемый цвет объекта
        body['data']['size']  # Ожидаемый размер объекта
    )


# Тест для негативных сценариев (400)
@pytest.mark.parametrize("test_data", NEGATIVE_TEST_DATA)  # Используем все негативные данные
def test_create_object_negative_cases(test_data, create_object_endpoint):
    # Извлекаем тело запроса из тестовых данных
    body = test_data['body']
    # Отправляем POST запрос с некорректными данными
    create_object_endpoint.create_object(body=body)
    # Проверяем, что статус код ответа равен 400 (ошибка клиента)
    create_object_endpoint.check_bad_request()


# Тест для проверки ошибок "не найдено" (404)
@pytest.mark.parametrize("test_data", NOT_FOUND_TEST_DATA)
def test_create_object_not_found(test_data, create_object_endpoint):
    # Извлекаем тело запроса и URL из тестовых данных
    body = test_data['body']
    wrong_url = test_data['url']

    # Отправляем POST запрос на неправильный URL
    create_object_endpoint.url = wrong_url
    create_object_endpoint.create_object(body=body)

    # Используем метод из родительского класса Endpoint для проверки ошибки 404
    create_object_endpoint.check_not_found_error()


# Тест полного обновления объекта (PUT запрос)
def test_put_object(complete_object_update_endpoint, new_object_id):
    # Тело запроса для полного обновления объекта
    body = {
        'data': {
            'color': 'yellow',
            'size': 'very big'
        },
        'id': new_object_id,
        'name': 'Second new object'
    }
    # Выполняем полное обновление объекта
    complete_object_update_endpoint.make_changes_object(new_object_id, body)
    # Проверяем, что объект успешно обновлен
    complete_object_update_endpoint.verify_object_successfully(
        body['name'],  # Ожидаемое имя объекта
        body['data']['color'],  # Ожидаемый цвет объекта
        body['data']['size']  # Ожидаемый размер объекта
    )


# Тест частичного обновления объекта (PATCH запрос)
def test_patch_object(partial_object_update_endpoint, new_object_id):
    # Обновляем только имя, цвет и размер должны остаться прежними
    body = {'name': 'Third new object - updated name only'}
    # Выполняем частичное обновление объекта
    partial_object_update_endpoint.partial_update_object(new_object_id, body)
    # Проверяем, что объект успешно обновлен
    # Ожидаем новое имя, но старые значения цвета и размера
    # Метод verify_object_successfully() уже проверяет статус код 200 внутри себя
    partial_object_update_endpoint.verify_object_successfully(
        'Third new object - updated name only',  # Новое имя
        'red',  # Цвет должен остаться как в фикстуре
        'big'  # Размер должен остаться как в фикстуре
    )


# Тест удаления объекта
def test_delete_object(delete_object_endpoint, new_object_id):
    # Удаляем объект по ID
    delete_object_endpoint.delete_object_by_id(new_object_id)
    # Проверяем, что удаление прошло успешно (статус 200)
    delete_object_endpoint.verify_object_deleted_successfully()
    # Проверяем, что объект действительно удален (статус 404 при попытке получить)
    delete_object_endpoint.verify_object_not_found(new_object_id)
