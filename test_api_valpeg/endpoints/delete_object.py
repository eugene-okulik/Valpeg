import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step("Отправка DELETE запроса для удаления объекта")
    def delete_object_by_id(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        return self.response

    @allure.step("Проверка успешного удаления объекта")
    def verify_object_deleted_successfully(self):
        assert self.response.status_code == 200, f"Expected status code 200, but got {self.response.status_code}"

    @allure.step("Проверка что объект действительно удален")
    def verify_object_not_found(self, object_id):
        check_response = requests.get(f'{self.url}/{object_id}')
        assert check_response.status_code == 404, f"Expected status code 404 after deletion, but got {check_response.status_code}"