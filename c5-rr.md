## 5 processes
## Using Round-Robin
## Quantum   3

| **Time** | **Process** | **Action** |
|:-:|:-:|:-:|
|   0 | `P1` | arrived |
|   0 | `P1` | selected (burst   5) |
|   2 | `P2` | arrived |
|   3 | `P2` | selected (burst   9) |
|   6 | `P1` | selected (burst   2) |
|   8 | `P1` | **finished** |
|   8 | `P2` | selected (burst   6) |
|   9 | `P3` | arrived |
|  11 | `P5` | arrived |
|  11 | `P3` | selected (burst   3) |
|  14 | `P4` | arrived |
|  14 | `P3` | **finished** |
|  14 | `P5` | selected (burst   1) |
|  15 | `P5` | **finished** |
|  15 | `P2` | selected (burst   3) |
|  18 | `P2` | **finished** |
|  18 | `P4` | selected (burst   4) |
|  21 | `P4` | selected (burst   1) |
|  22 | `P4` | **finished** |
|  22 | N/A | Idle |
|  23 | N/A | Idle |
|  24 | N/A | Idle |

**Finished at time  25**

## Times
| **Process** | **Wait** | **Turnaround** | **Response** |
|:-:|:-:|:-:|:-:|
| `P1` |   3 |   8 |   0 |
| `P2` |   7 |  16 |   1 |
| `P3` |   2 |   5 |   2 |
| `P4` |   4 |   8 |   4 |
| `P5` |   3 |   4 |   3 |

