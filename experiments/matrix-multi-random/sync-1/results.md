# Pod lifecicle
| Pod name                    | execution mode | creation timestamp   |
|-----------------------------|----------------|----------------------|
| matrix-multiplication-00001 | cpu_preferred  | 2025-07-31T09:19:04Z |
| matrix-multiplication-00002 | gpu_preferred  | 2025-07-31T09:31:42Z |

end: 2025-07-31T09:58:05.42Z


# Questions - Observations
1. Irgendwie dauert es beim zweiten auf GPU wechseln länger
2. Matrix size linie ist nicht linear, weil die responses nicht immer gleich lang sind (synchronous response)