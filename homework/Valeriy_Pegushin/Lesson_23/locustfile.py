from locust import HttpUser, task
import random


class LoadTestUser(HttpUser):
    new_id = None

    def on_start(self) -> None:
        response = self.client.post(
            '',
            json={
                'data': {
                    'color': 'red',
                    'size': 'big'
                },
                'name': 'First new object'
            }
        )
        self.new_id = response.json().get('id')

    @task(1)
    def get_one_object_test(self):
        if self.new_id:
            self.client.get(f'/{self.new_id}')

    @task(3)
    def get_one_object_test(self):
        # Просто выбираем один из трех ID
        object_id = random.choice([36, 204, 1971])
        self.client.get(f'/{object_id}')
