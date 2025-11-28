import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step("Проверка успешного создания/обновления объекта")
    def verify_object_successfully(self, name, color, size):
        assert self.response.status_code == 200, f"Expected status code 200, but got {self.response.status_code}"
        self.json = self.response.json()
        assert self.json['name'] == name
        assert self.json['data']['color'] == color
        assert self.json['data']['size'] == size

    @allure.step('Проверьте, что ответ — 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, f"Expected status code 200, but got {self.response.status_code}"

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400
