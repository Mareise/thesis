# Initial Setup
**Script = evaluation_script/sentiment-analysis/sentiment-analysis-with-breaks.py**
```python
loop(200)
time.sleep(60) # wait for a minute
loop(50)
time.sleep(60) # wait for a minute
loop(200)
```

## GPU Analyzer Params
```yaml
# Timing configuration (INTERVAL_SECONDS has to be significantly lower than WINDOW_MINUTES)
- name: INTERVAL_SECONDS # How often to check the metrics
  value: "30"
- name: WINDOW_MINUTES # How long to consider the metrics
  value: "10"
- name: LOW_REQUEST_RATE_WINDOW_MINUTES # the window in which we consider the request rate to be low
  value: "30"

- name: LONG_INTERVAL_MULTIPLIER # Multiplier for a longer latency metrics interval
  value: "50"

# Logging configuration
- name: LOG_LEVEL
  value: "INFO"

# Thresholds
- name: THRESHOLD_LATENCY_UPPER # Upper latency threshold for execution mode change
  value: "1000"
- name: THRESHOLD_LATENCY_UPPER_WHEN_LOW_REQUEST_RATE # Upper latency threshold for switching back to cpu when request rate is low
  value: "2000"
- name: THRESHOLD_LATENCY_PERFORMANCE_CHANGE_GAP # Gap in latency to consider a performance change
  value: "200"

- name: THRESHOLD_REQUEST_RATE_COLD_START_MITIGATION # When request rate is below this, we dont take actions
  value: "0.2"

- name: THRESHOLD_REQUEST_RATE_LOWER_BOUND # Lower bound for request rate to consider switching to CPU
  value: "0.01"
```