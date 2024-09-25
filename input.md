## 2 processes
## Using First-Come First-Served

| **Time** | **Process** | **Action** |
|:-:|:-:|:-:|
|   0 | `A` | arrived |
|   0 | `A` | selected (burst   3) |
|   3 | `A` | **finished** |
|   2 | `B` | arrived |
|   3 | `B` | selected (burst   2) |
|   5 | `B` | **finished** |

**Finished at time 5**

## Times
| **Process** | **Wait** | **Turnaround** | **Response** |
|:-:|:-:|:-:|:-:|
| `A` |   0 |   3 |   0 |
| `B` |   1 |   3 |   1 |

