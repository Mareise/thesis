import requests
import time
import csv
import random
from datetime import datetime

url = "http://localhost:8080/matrix-multiplication"
min_size = 0
max_size = 20000
iterations = 500
wait_time = 2
csv_filename = "../visualization/matrix_multiplication-random.csv"

headers = {
    "Content-Type": "application/json",
    "Host": "matrix-multiplication.default.128.131.172.200.sslip.io"
}

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "matrix_size", "response_time_ms"])

for _ in range(iterations):
    matrix_size = random.randint(min_size, max_size)
    payload = {"matrix_size": matrix_size}
    start_time = time.time()

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        end_time = time.time()
        response_time_ms = (end_time - start_time) * 1000
    except requests.RequestException as e:
        print(f"Request failed for size {matrix_size}: {e}")
        response_time_ms = -1  # Use -1 to indicate failure

    timestamp = datetime.utcnow().isoformat()
    row = [timestamp, matrix_size, response_time_ms]

    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

    print(f"Sent size {matrix_size}, response time: {response_time_ms:.2f} ms")
    time.sleep(wait_time)
