**2** processes
Using **Round-Robin**
Quantum   **2**

## Timeline
| **Time** | **Process** | **Action** |
|:-:|:-:|:-:|
|   0 | `P2` | arrived |
|   0 | `P2` | selected (burst   9) |
|   2 | `P2` | selected (burst   7) |
|   3 | `P1` | arrived |
|   4 | `P1` | selected (burst   5) |
|   6 | `P2` | selected (burst   5) |
|   8 | `P1` | selected (burst   3) |
|  10 | `P2` | selected (burst   3) |
|  12 | `P1` | selected (burst   1) |
|  13 | `P1` | **finished** |
|  13 | `P2` | selected (burst   1) |
|  14 | `P2` | **finished** |
|  14 | N/A | Idle |

**Finished at time  15**

## Metrics
| **Process** | **Wait** | **Turnaround** | **Response** |
|:-:|:-:|:-:|:-:|
| `P1` |   5 |  10 |   1 |
| `P2` |   5 |  14 |   0 |
