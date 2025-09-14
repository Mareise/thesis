# Static Analysis Results
```shell
Analysis Result for func.py:
  Execution Mode: cpu_preferred
  Reason: Detected 1 relevant imports.
  Details:
    Imports: [torch]
    Uses CUDA: false
    Lines Considered: []

Analysis Result for __init__.py:
  Execution Mode: cpu
  Reason: No GPU-related calls or imports detected.
  Details:
    Imports: []
    Uses CUDA: false
    Lines Considered: []

Analysis Result for main.py:
  Execution Mode: cpu
  Reason: No GPU-related calls or imports detected.
  Details:
    Imports: []
    Uses CUDA: false
    Lines Considered: []
Set execution mode to: cpu_preferred
```
# Pod lifecicle
| Pod name                    | execution mode | creation timestamp   |
|-----------------------------|----------------|----------------------|
| matrix-multiplication-00001 | cpu_preferred  | 2025-07-28T14:02:35Z |
| matrix-multiplication-00002 | gpu_preferred  | 2025-07-28T14:09:01Z |
| matrix-multiplication-00003 | cpu_preferred  | 2025-07-28T14:10:01Z |
| matrix-multiplication-00004 | gpu_preferred  | 2025-07-28T14:11:00Z |

end: 2025-07-28T14:13:28.30Z


# Questions - Observations
1. Irgendwie dauert es beim zweiten auf GPU wechseln länger
2. Matrix size linie ist nicht linear, weil die responses nicht immer gleich lang sind (synchronous response)
