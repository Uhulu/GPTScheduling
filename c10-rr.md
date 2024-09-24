## 10 processes
## Using Round-Robin
## Quantum   3

| **Time** | **Process** | **Action** |
|:-:|:-:|:-:|
|   0 | `P01` | arrived |
|   0 | `P01` | selected (burst   5) |
|   3 | `P01` | selected (burst   2) |
|   5 | `P02` | arrived |
|   5 | `P01` | **finished** |
|   5 | `P02` | selected (burst   9) |
|   7 | `P03` | arrived |
|   8 | `P03` | selected (burst   3) |
|   9 | `P04` | arrived |
|  10 | `P05` | arrived |
|  11 | `P03` | **finished** |
|  11 | `P02` | selected (burst   6) |
|  12 | `P07` | arrived |
|  14 | `P04` | selected (burst   4) |
|  17 | `P05` | selected (burst   8) |
|  20 | `P07` | selected (burst   5) |
|  23 | `P06` | arrived |
|  23 | `P02` | selected (burst   3) |
|  25 | `P08` | arrived |
|  26 | `P02` | **finished** |
|  26 | `P04` | selected (burst   1) |
|  27 | `P04` | **finished** |
|  27 | `P05` | selected (burst   5) |
|  30 | `P09` | arrived |
|  30 | `P06` | selected (burst   4) |
|  33 | `P07` | selected (burst   2) |
|  34 | `P10` | arrived |
|  35 | `P07` | **finished** |
|  35 | `P08` | selected (burst   4) |
|  38 | `P09` | selected (burst   7) |
|  41 | `P05` | selected (burst   2) |
|  43 | `P05` | **finished** |
|  43 | `P06` | selected (burst   1) |
|  44 | `P06` | **finished** |
|  44 | `P10` | selected (burst  10) |
|  47 | `P08` | selected (burst   1) |
|  48 | `P08` | **finished** |
|  48 | `P09` | selected (burst   4) |
|  51 | `P10` | selected (burst   7) |
|  54 | `P09` | selected (burst   1) |
|  55 | `P09` | **finished** |
|  55 | `P10` | selected (burst   4) |
|  58 | `P10` | selected (burst   1) |
|  59 | `P10` | **finished** |
|  59 | N/A | Idle |

**Finished at time  60**

## Times
| **Process** | **Wait** | **Turnaround** | **Response** |
|:-:|:-:|:-:|:-:|
| `P01` |   0 |   5 |   0 |
| `P02` |  12 |  21 |   0 |
| `P03` |   1 |   4 |   1 |
| `P04` |  14 |  18 |   5 |
| `P05` |  25 |  33 |   7 |
| `P06` |  17 |  21 |   7 |
| `P07` |  18 |  23 |   8 |
| `P08` |  19 |  23 |  10 |
| `P09` |  18 |  25 |   8 |
| `P10` |  15 |  25 |  10 |

