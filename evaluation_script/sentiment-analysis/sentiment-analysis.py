import requests
import time
import csv
import json
from datetime import datetime

url = "http://localhost:8080/sentiment-analysis"
iterations = 500
wait_time = 0
csv_filename = "../sentiment-analysis-1.csv"

headers = {
    "Content-Type": "application/json",
    "Host": "sentiment-analysis.default.128.131.172.200.sslip.io"
}

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "response_time_ms"])

with open('payload.json', 'r') as file:
    payload = json.load(file)

# Loop over matrix sizes
for _ in range(iterations):
    start_time = time.time()

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        end_time = time.time()
        response_time_ms = (end_time - start_time) * 1000
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        response_time_ms = -1  # Use -1 to indicate failure

    timestamp = datetime.utcnow().isoformat()
    row = [timestamp, response_time_ms]

    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

    print(f"Response time: {response_time_ms:.2f} ms")
    time.sleep(wait_time)
