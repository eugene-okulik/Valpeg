# Импорт необходимых библиотек
import requests  # Библиотека для отправки HTTP запросов
import allure    # Библиотека для создания детальных отчетов о тестировании
from endpoints.endpoint import Endpoint

# Класс для работы с endpoint создания объектов
class CreateObject(Endpoint):

    # Метод для отправки POST запроса на создание объекта
    @allure.step("Отправка POST запроса для создания объекта")  # Декоратор для создания шага в отчете Allure
    def create_object(self, body, headers=None):
        # Используем переданные заголовки или заголовки по умолчанию
        headers = headers if headers else self.headers
        # Отправляем POST запрос на указанный URL
        self.response = requests.post(
            self.url,      # URL endpoint
            json=body,     # Тело запроса в формате JSON
            headers=headers # Заголовки запроса
        )
        # Возвращаем объект ответа
        return self.response


    # Метод для проверки неудачного создания объекта
    @allure.step("Проверка ошибки создания объекта")  # Декоратор для создания шага в отчете Allure
    def verify_object_creation_failed(self):
        # Проверяем только статус код 400 (ошибка клиента)
        assert self.response.status_code == 400, f"Expected status code 400, but got {self.response.status_code}"

    # Метод для проверки ошибки "не найдено" (404)
    @allure.step("Проверка ошибки 'не найдено' (404)")
    def verify_not_found_error(self):
        assert self.response.status_code == 404, f"Expected status code 404, but got {self.response.status_code}"
