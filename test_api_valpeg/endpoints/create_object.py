# Импорт необходимых библиотек
import requests  # Библиотека для отправки HTTP запросов
import allure    # Библиотека для создания детальных отчетов о тестировании
from endpoints.endpoint import Endpoint


# Класс для работы с endpoint создания объектов
class CreateObject(Endpoint):

    # Метод для отправки POST запроса на создание объекта
    @allure.step("Отправка POST запроса для создания объекта")
    def create_object(self, body, headers=None):
        # Используем переданные заголовки или заголовки по умолчанию
        headers = headers if headers else self.headers
        # Отправляем POST запрос на указанный URL
        self.response = requests.post(
            self.url,  # URL endpoint
            json=body,  # Тело запроса в формате JSON
            headers=headers  # Заголовки запроса
        )
        # Возвращаем объект ответа
        return self.response
