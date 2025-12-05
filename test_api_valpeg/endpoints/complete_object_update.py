import requests
import allure
from endpoints.endpoint import Endpoint


class CompleteObjectUpdate(Endpoint):  # Исправлено имя класса

    @allure.step("Отправка PUT запроса для обновления объекта")
    def make_changes_object(self, object_id, body, headers=None):  # Исправлено имя параметра
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{object_id}',  # Исправлено имя параметра
            json=body,
            headers=headers
        )
        self.json = self.response.json()
