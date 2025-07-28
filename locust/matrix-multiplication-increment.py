from locust import HttpUser, task, between
import random
from datetime import datetime

class KnativeUser(HttpUser):
    wait_time = between(2, 2)

    @task
    def call_matrix_multiplication(self):
        if not hasattr(self, "matrix_size"):
            self.matrix_size = 0
        else:
            self.matrix_size = min(self.matrix_size + 100, 20000)
        matrix_size = self.matrix_size
        print(f"{datetime.now().isoformat()} - {matrix_size}")
        self.client.post(
            "/matrix-multiplication",
            headers={
            "Host": "matrix-multiplication.default.128.131.172.200.sslip.io"
            },
            json={
            "matrix_size": matrix_size
            }
        )


