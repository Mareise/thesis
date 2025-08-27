# Initial Setup
**Script = evaluation_script/matrix-multiplication-increment-async.py**

**Wait time = 2s**

**Start Size = 0**

**Increment = 100**

**End Size = 20000**

## GPU Analyzer Params
```yaml
# Timing configuration (interval has to be significantly lower than window)
- name: INTERVAL_SECONDS
  value: "30"
- name: WINDOW_MINUTES
  value: "10"

# Logging configuration
- name: LOG_LEVEL
  value: "INFO"

# Thresholds
- name: THRESHOLD_LATENCY_UPPER
  value: "1000"
- name: THRESHOLD_LATENCY_UPPER_WHEN_LOW_REQUEST_RATE
  value: "2000"
- name: THRESHOLD_LATENCY_PERFORMANCE_CHANGE_GAP
  value: "200"

- name: THRESHOLD_REQUEST_RATE_LOWER_BOUND
  value: "0.01"
- name: LOW_REQUEST_RATE_SWITCHING_MINUTES
  value: "30"

- name: LONG_INTERVAL_WINDOW_MINUTES
  value: "500"
```