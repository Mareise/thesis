import requests
import time
import csv
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

# Configuration
url = "http://localhost:8080/matrix-multiplication"
headers = {
    "Content-Type": "application/json",
    "Host": "matrix-multiplication.default.128.131.172.200.sslip.io"
}
csv_filename = "../matrix_benchmark.csv"
start_size = 0
end_size = 20000
step = 100
delay = 2

write_lock = Lock()

with open(csv_filename, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "matrix_size", "response_time_ms"])


# Function to send a request
def send_request(matrix_size):
    payload = {"matrix_size": matrix_size}
    start_time = time.time()
    timestamp = datetime.utcnow().isoformat()

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        response_time_ms = (time.time() - start_time) * 1000
    except requests.RequestException as e:
        print(f"Error for size {matrix_size}: {e}")
        response_time_ms = -1

    row = [timestamp, matrix_size, response_time_ms]

    # Thread-safe CSV write
    with write_lock:
        with open(csv_filename, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(row)

    print(f"Sent size {matrix_size}, response: {response_time_ms:.2f} ms")


# Launch threads without waiting
with ThreadPoolExecutor(max_workers=10) as executor:
    for matrix_size in range(start_size, end_size + 1, step):
        executor.submit(send_request, matrix_size)
        time.sleep(delay)
