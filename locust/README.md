# Locust testing
```
locust -f locust.py --host=http://localhost:8080 --csv-full-history
locust -f matrix-multiplication-random.py --host=http://localhost:8080 --csv-full-history
locust -f matrix-multiplication-increment.py --host=http://localhost:8080 --csv-full-history --csv matrix-multiplication-increment-full-history
```