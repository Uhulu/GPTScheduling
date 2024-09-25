**10** processes
Using **First-Come First-Served**

## Timeline
| **Time** | **Process** | **Action** |
|:-:|:-:|:-:|
|   0 | `P01` | arrived |
|   0 | `P01` | selected (burst   5) |
|   5 | `P01` | **finished** |
|   1 | `P04` | arrived |
|   5 | `P02` | arrived |
|   5 | `P04` | selected (burst   4) |
|   9 | `P04` | **finished** |
|   9 | `P03` | arrived |
|   9 | `P02` | selected (burst   9) |
|  18 | `P02` | **finished** |
|  10 | `P05` | arrived |
|  12 | `P07` | arrived |
|  13 | `P10` | arrived |
|  18 | `P03` | selected (burst   3) |
|  21 | `P03` | **finished** |
|  21 | `P05` | selected (burst   8) |
|  29 | `P05` | **finished** |
|  23 | `P06` | arrived |
|  25 | `P08` | arrived |
|  29 | `P07` | selected (burst   5) |
|  34 | `P07` | **finished** |
|  30 | `P09` | arrived |
|  34 | `P10` | selected (burst   2) |
|  36 | `P10` | **finished** |
|  36 | `P06` | selected (burst   4) |
|  40 | `P06` | **finished** |
|  40 | `P08` | selected (burst   4) |
|  44 | `P08` | **finished** |
|  44 | `P09` | selected (burst   7) |
|  51 | `P09` | **finished** |
|  51 | N/A | Idle |
|  52 | N/A | Idle |
|  53 | N/A | Idle |
|  54 | N/A | Idle |

**Finished at time 55**

## Metrics
| **Process** | **Wait** | **Turnaround** | **Response** |
|:-:|:-:|:-:|:-:|
| `P01` |   0 |   5 |   0 |
| `P02` |   4 |  13 |   4 |
| `P03` |   9 |  12 |   9 |
| `P04` |   4 |   8 |   4 |
| `P05` |  11 |  19 |  11 |
| `P06` |  13 |  17 |  13 |
| `P07` |  17 |  22 |  17 |
| `P08` |  15 |  19 |  15 |
| `P09` |  14 |  21 |  14 |
| `P10` |  21 |  23 |  21 |

