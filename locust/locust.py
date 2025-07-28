from locust import HttpUser, task, between

class KnativeUser(HttpUser):
    wait_time = between(3, 3)

    # @task
    # def call_simple_cpu(self):
    #     self.client.get(
    #         "/cpu",
    #         headers={
    #             "Host": "wasgeht.default.128.131.172.200.sslip.io"
    #         }
    #     )

    @task
    def call_gpu(self):
        self.client.get(
            "/gpu",
            headers={
                "Host": "gpu-function.default.128.131.172.200.sslip.io"
            }
        )

    # @task
    # def call_matrix_multiplication(self):
    #     self.client.post(
    #         "/matrix-multiplication",
    #         headers={
    #             "Host": "matrix-multiplication.default.128.131.172.200.sslip.io"
    #         },
    #         json={
    #             "matrix_size": 20480
    #         }
    #     )


