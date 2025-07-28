from locust import HttpUser, task, between
import random

class KnativeUser(HttpUser):
    wait_time = between(3, 3)

    @task
    def call_matrix_multiplication(self):
        matrix_size = random.randint(200, 20480)
        self.client.post(
            "/matrix-multiplication",
            headers={
            "Host": "matrix-multiplication.default.128.131.172.200.sslip.io"
            },
            json={
            "matrix_size": matrix_size
            }
        )


