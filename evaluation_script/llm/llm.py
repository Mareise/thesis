import requests
import time
import csv
import json
from datetime import datetime

url = "http://localhost:8080/llm"
iterations = 500
wait_time = 100
runs = 3  # number of times to repeat the experiment

headers = {
    "Content-Type": "application/json",
    "Host": "llm.default.128.131.172.200.sslip.io"
}

with open('payload.json', 'r') as file:
    payload = json.load(file)

# print start time

for run in range(1, runs + 1):
    print(f"Run {run}: Starting at {datetime.utcnow().isoformat()} UTC")
    csv_filename = f"../llm-cpu-{run}.csv"

    # create new CSV file with header
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "response_time_ms"])

    print(f"\n=== Run {run} -> Saving to {csv_filename} ===")

    # Loop over iterations
    for i in range(iterations):
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

        # append to CSV
        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

        print(f"[Run {run}] Iteration {i+1}/{iterations} - Response time: {response_time_ms:.2f} ms")

    time.sleep(wait_time) # wait so that the pod can scale down

print(f"\nFinished all {runs} runs at {datetime.utcnow().isoformat()} UTC")
