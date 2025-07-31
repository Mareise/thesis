# Initial Setup
**Script = evaluation_script/matrix-multiplication-random.py**

**Wait time = 2s**

**Min Size = 0**

**Max Size = 20000**

**Number of iterations = 500**

## GPU Analyzer Params
```yaml
# Timing configuration (interval has to be significantly lower than window)
- name: INTERVAL_SECONDS
  value: "60"
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

- name: LONG_INTERVAL_MULTIPLIER
  value: "50"
```