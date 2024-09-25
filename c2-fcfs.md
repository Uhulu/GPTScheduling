**2** processes
Using **First-Come First-Served**

## Timeline
| **Time** | **Process** | **Action** |
|:-:|:-:|:-:|
|   0 | `P1` | arrived |
|   0 | `P1` | selected (burst   5) |
|   5 | `P1` | **finished** |
|   5 | N/A | Idle |
|   6 | N/A | Idle |
|   7 | `P2` | arrived |
|   7 | `P2` | selected (burst   9) |
|  16 | `P2` | **finished** |
|  16 | N/A | Idle |
|  17 | N/A | Idle |
|  18 | N/A | Idle |
|  19 | N/A | Idle |

**Finished at time 20**

## Metrics
| **Process** | **Wait** | **Turnaround** | **Response** |
|:-:|:-:|:-:|:-:|
| `P1` |   0 |   5 |   0 |
| `P2` |   0 |   9 |   0 |

