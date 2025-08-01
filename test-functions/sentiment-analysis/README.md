# Python HTTP Function

Welcome to your new Python Function! A minimal Function implementation can
be found in func.py.

For more, see [the complete documentation]('https://github.com/knative/func/tree/main/docs')

# Call it
```
curl -X POST http://sentiment-analysis.default.128.131.172.200.sslip.io/ -H "Content-Type: application/json" -d '{"text": "I really love how simple this is!?"}'
```