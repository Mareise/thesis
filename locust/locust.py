from locust import HttpUser, task, between

class KnativeUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def call_knative_service(self):
        self.client.get(
            "/",
            headers={
                "Host": "wasgeht.default.128.131.172.200.sslip.io"
            }
        )
    
