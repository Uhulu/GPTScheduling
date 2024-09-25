**10** processes
Using **Preemptive Shortest Job First**
## Timeline
| **Time** | **Process** | **Action** |
|:-:|:-:|:-:|
|   0 | `P01` | arrived |
|   0 | `P01` | selected (burst 5) |
|   5 | `P02` | arrived |
|   5 | `P01` | **finished** |
|   5 | `P02` | selected (burst 9) |
|   9 | `P03` | arrived |
|   9 | `P03` | selected (burst 3) |
|  10 | `P04` | arrived |
|  11 | `P05` | arrived |
|  12 | `P06` | arrived |
|  12 | `P03` | **finished** |
|  12 | `P04` | selected (burst 4) |
|  16 | `P04` | **finished** |
|  16 | `P06` | selected (burst 4) |
|  18 | `P07` | arrived |
|  20 | `P06` | **finished** |
|  20 | `P02` | selected (burst 5) |
|  25 | `P08` | arrived |
|  25 | `P02` | **finished** |
|  25 | `P08` | selected (burst 4) |
|  29 | `P08` | **finished** |
|  29 | `P07` | selected (burst 5) |
|  30 | `P09` | arrived |
|  34 | `P10` | arrived |
|  34 | `P07` | **finished** |
|  34 | `P09` | selected (burst 7) |
|  41 | `P09` | **finished** |
|  41 | `P05` | selected (burst 8) |
|  49 | `P05` | **finished** |
|  49 | `P10` | selected (burst 10) |
|  59 | `P10` | **finished** |
|  59 | N/A | Idle |

**Finished at time 60**

## Metrics
| **Process** | **Wait** | **Turnaround** | **Response** |
|:-:|:-:|:-:|:-:|
| `P01` |   0 |   5 |   0 |
| `P02` |  11 |  20 |   0 |
| `P03` |   0 |   3 |   0 |
| `P04` |   2 |   6 |   2 |
| `P05` |  30 |  38 |  30 |
| `P06` |   4 |   8 |   4 |
| `P07` |  11 |  16 |  11 |
| `P08` |   0 |   4 |   0 |
| `P09` |   4 |  11 |   4 |
| `P10` |  15 |  25 |  15 |

