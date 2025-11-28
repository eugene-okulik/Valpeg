# Импорт библиотеки для отправки HTTP-запросов
import requests
# Импорт библиотеки для создания детальных отчетов о тестировании
import allure
# Импорт базового класса эндпоинта
from endpoints.endpoint import Endpoint


# Класс для работы с endpoint удаления объектов
class DeleteObject(Endpoint):

    # Метод отправки DELETE запроса для удаления объекта по ID
    @allure.step("Отправка DELETE запроса для удаления объекта")
    def delete_object_by_id(self, object_id):
        # Отправка DELETE запроса по URL с указанным ID объекта
        self.response = requests.delete(f'{self.url}/{object_id}')
        # Возврат объекта ответа от сервера
        return self.response

    # Метод проверки успешного удаления объекта
    @allure.step("Проверка успешного удаления объекта")
    def verify_object_deleted_successfully(self):
        # Проверка, что статус код ответа равен 200 (Успех)
        assert self.response.status_code == 200, (
            # Сообщение об ошибке, если статус код не соответствует ожидаемому
            f"Expected status code 200, but got {self.response.status_code}"
        )

    # Метод проверки, что объект действительно удален (не найден)
    @allure.step("Проверка что объект действительно удален")
    def verify_object_not_found(self, object_id):
        # Отправка GET запроса для проверки существования объекта
        check_response = requests.get(f'{self.url}/{object_id}')
        # Проверка, что статус код ответа равен 404 (Не найдено)
        assert check_response.status_code == 404, (
            # Сообщение об ошибке, если объект все еще существует
            f"Expected status code 404 after deletion, but got "
            f"{check_response.status_code}"
        )
