## 5 processes
## Using Preemptive Shortest Job First
| **Time** | **Process** | **Action** |
|:-:|:-:|:-:|
|   0 | `P1` | arrived |
|   0 | `P1` | selected (burst 5) |
|   2 | `P2` | arrived |
|   5 | `P1` | **finished** |
|   5 | `P2` | selected (burst 9) |
|   7 | `P4` | arrived |
|   7 | `P4` | selected (burst 4) |
|   9 | `P3` | arrived |
|  11 | `P4` | **finished** |
|  11 | `P5` | arrived |
|  11 | `P5` | selected (burst 1) |
|  12 | `P5` | **finished** |
|  12 | `P3` | selected (burst 3) |
|  15 | `P3` | **finished** |
|  15 | `P2` | selected (burst 7) |
|  22 | `P2` | **finished** |
|  22 | N/A | Idle |
|  23 | N/A | Idle |
|  24 | N/A | Idle |

**Finished at time 25**

## Times
| **Process** | **Wait** | **Turnaround** | **Response** |
|:-:|:-:|:-:|:-:|
| `P1` |   0 |   5 |   0 |
| `P2` |  11 |  20 |   3 |
| `P3` |   3 |   6 |   3 |
| `P4` |   0 |   4 |   0 |
| `P5` |   0 |   1 |   0 |
