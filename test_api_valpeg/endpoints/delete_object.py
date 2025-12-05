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
        # Используем метод из родительского класса для проверки статус-кода 200
        self.check_that_status_is_200()

    # Метод проверки, что объект действительно удален (не найден)
    @allure.step("Проверка что объект действительно удален")
    def verify_object_not_found(self, object_id):
        # Отправка GET запроса для проверки существования объекта
        check_response = requests.get(f'{self.url}/{object_id}')
        # Сохраняем response в self.response для использования метода из родительского класса
        self.response = check_response
        # Используем метод из родительского класса для проверки статус-кода 404
        self.check_not_found_error()
