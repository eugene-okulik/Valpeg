import requests
import allure
from endpoints.endpoint import Endpoint


class PartialObjectUpdate(Endpoint):

    @allure.step("Отправка PATCH запроса для частичного обновления объекта")
    def partial_update_object(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{object_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.json
