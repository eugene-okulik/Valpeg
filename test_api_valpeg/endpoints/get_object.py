import requests
import allure
from endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step("Отправка GET запроса для получения объекта")
    def get_object_by_id(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        self.json = self.response.json()
        return self.json

    @allure.step("Проверка что получен правильный объект")
    def verify_object_id_matches(self, expected_id):
        self.check_that_status_is_200()
        assert self.json['id'] == expected_id, f"Expected ID {expected_id}, but got {self.json['id']}"
