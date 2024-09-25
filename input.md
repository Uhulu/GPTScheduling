**2** processes
Using **Preemptive Shortest Job First**
## Timeline
| **Time** | **Process** | **Action** |
|:-:|:-:|:-:|
|   0 | `A` | arrived |
|   0 | `A` | selected (burst 3) |
|   2 | `B` | arrived |
|   3 | `A` | **finished** |
|   3 | `B` | selected (burst 3) |

**Finished at time 5**

## Metrics
| **Process** | **Wait** | **Turnaround** | **Response** |
|:-:|:-:|:-:|:-:|
| `A` |   0 |   3 |   0 |

`B` _did not finish_
