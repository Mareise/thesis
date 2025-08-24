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
| matrix-multiplication-00001 | cpu_preferred  | 2025-08-13T09:30:35Z |
| matrix-multiplication-00002 | gpu_preferred  | 2025-08-13T09:31:34Z |

end: 2025-08-13T09:33:11Z

CPU time = 09:31:34Z - 09:30:35Z = 59s
GPU time = 09:33:11Z - 09:31:34Z = 97s

Cost = 59 * 1 + 97 * 3.5 = 398.5
Cost = 59 * 0.000038 + 97 * 0.000133 = ca. 0.015