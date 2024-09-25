**5** processes
Using **First-Come First-Served**

## Timeline
| **Time** | **Process** | **Action** |
|:-:|:-:|:-:|
|   0 | `P2` | arrived |
|   0 | `P2` | selected (burst   9) |
|   9 | `P2` | **finished** |
|   7 | `P1` | arrived |
|   8 | `P4` | arrived |
|   9 | `P3` | arrived |
|   9 | `P1` | selected (burst   5) |
|  14 | `P1` | **finished** |
|  11 | `P5` | arrived |
|  14 | `P4` | selected (burst   4) |
|  18 | `P4` | **finished** |
|  18 | `P3` | selected (burst   3) |
|  21 | `P3` | **finished** |
|  21 | `P5` | selected (burst   1) |
|  22 | `P5` | **finished** |
|  22 | N/A | Idle |
|  23 | N/A | Idle |
|  24 | N/A | Idle |

**Finished at time 25**

## Metrics
| **Process** | **Wait** | **Turnaround** | **Response** |
|:-:|:-:|:-:|:-:|
| `P1` |   2 |   7 |   2 |
| `P2` |   0 |   9 |   0 |
| `P3` |   9 |  12 |   9 |
| `P4` |   6 |  10 |   6 |
| `P5` |  10 |  11 |  10 |

