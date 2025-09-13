import requests
import time
import csv
from datetime import datetime

url = "http://localhost:8080/idle-wait"

iterations = 200
idletime = 2
wait_time = 100
runs = 1  # number of times to repeat the experiment
payload = {"wait_time": idletime}

headers = {
    "Content-Type": "application/json",
    "Host": "idle-wait.default.128.131.172.200.sslip.io"
}

# Print start time in local time and not in UTC
print(f"Starting at {datetime.now().isoformat()} Local Time")


for run in range(1, runs + 1):
    print(f"Run {run}: Starting at {datetime.now().isoformat()} Local Time")
    csv_filename = f"../idle-wait-{run}.csv"

    # create new CSV file with header
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "response_time_ms", "gpu_used"])

    print(f"\n=== Run {run} -> Saving to {csv_filename} ===")

    # Loop over iterations
    for i in range(iterations):
        start_time = time.time()

        data = {}

        try:
            response = requests.post(url, json=payload, headers=headers)
            data = response.json()
            response.raise_for_status()
            end_time = time.time()
            response_time_ms = (end_time - start_time) * 1000
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            response_time_ms = -1  # Use -1 to indicate failure

        timestamp = datetime.now().isoformat()
        row = [timestamp, response_time_ms, data.get("gpu", "N/A")]

        # append to CSV
        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

        print(f"[Run {run}] Iteration {i+1}/{iterations} - Response time: {response_time_ms:.2f} ms - GPU used: {data.get('gpu', 'N/A')}")

    time.sleep(wait_time) # wait so that the pod can scale down

print(f"\nFinished all {runs} runs at {datetime.now().isoformat()} Local Time")
