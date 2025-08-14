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
Set execution mode to: gpu
```
# Pod lifecicle
| Pod name                    | execution mode | creation timestamp   |
|-----------------------------|----------------|----------------------|
| matrix-multiplication-00001 | gpu  | 2025-08-13T09:58:38.375866 |

end: 2025-08-13T10:00:37.211328

Time = 10:00:37 - 09:58:38 = 119s

Cost = 119 * 3.5 = 416.5