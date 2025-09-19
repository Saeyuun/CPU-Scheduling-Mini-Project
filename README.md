# Mini CPU Scheduler Simulation

A CPU Scheduler Simulation that demonstrates how different scheduling algorithms manage processes. It supports First-Come, First-Served (FCFS), Round Robin (RR) with default quantum of 2, and optionally Shortest Job First (SJF). The simulator produces a Gantt chart timeline, per-process metrics (waiting, turnaround, response times), and overall averages, letting you compare how algorithms affect performance.

  ## How to run
  * Locate the file location
  * Open Powershell or CMD

  Run any of these 3 command

  FCFS:
  ```bash
  py main.py --algo fcfs
  ```

  Round Robin with Time Quantum = 2
  ```bash
  py main.py --algo rr
  ```

  SJF (Non-preemptive)
  ```bash
  py main.py --algo sjf
  ```

  ## Expected Output
  Here is the predetermined data provided:
  | PID | Arrival Time | Burst Time |
  |-----|---------|-------|
  | P1  | 0       | 7     |
  | P2  | 2       | 4     |
  | P3  | 4       | 1     |
  | P4  | 5       | 4     |
  | P5  | 6       | 3     |


  ### First Come First Serve (FCFS)
  ```java
Scheduling Results: FIRST COME FIRST SERVE

╒═════════╤════════════════╤══════════════╤═══════════════════╤═════════╤════════════════╤════════════════════╤═════════════════╕
│   PID   │  Arrival Time  │  Burst Time  │  Completion Time  │  Start  │  Waiting Time  │  Turn Around Time  │  Response Time  │
╞═════════╪════════════════╪══════════════╪═══════════════════╪═════════╪════════════════╪════════════════════╪═════════════════╡
│   P1    │       0        │      7       │         7         │    0    │       0        │         7          │        0        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P2    │       2        │      4       │        11         │    7    │       5        │         9          │        5        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P3    │       4        │      1       │        12         │   11    │       7        │         8          │        7        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P4    │       5        │      4       │        16         │   12    │       7        │         11         │        7        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P5    │       6        │      3       │        19         │   16    │       10       │         13         │       10        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│ Average │                │              │                   │         │      5.8       │        9.6         │       5.8       │
╘═════════╧════════════════╧══════════════╧═══════════════════╧═════════╧════════════════╧════════════════════╧═════════════════╛

Gantt Chart
[P1:0–7][P2:7–11][P3:11–12][P4:12–16][P5:16–19]
  ```

  ### Round Robin with Time Quantum of 2
  ```java
  Scheduling Results: ROUND ROBIN (q=2)

╒═════════╤════════════════╤══════════════╤═══════════════════╤═════════╤════════════════╤════════════════════╤═════════════════╕
│   PID   │  Arrival Time  │  Burst Time  │  Completion Time  │  Start  │  Waiting Time  │  Turn Around Time  │  Response Time  │
╞═════════╪════════════════╪══════════════╪═══════════════════╪═════════╪════════════════╪════════════════════╪═════════════════╡
│   P1    │       0        │      7       │        19         │    0    │      12        │        19          │        0        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P2    │       2        │      4       │         9         │    2    │       3        │         7          │        0        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P3    │       4        │      1       │         7         │    6    │       2        │         3          │        2        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P4    │       5        │      4       │        17         │    9    │       8        │        12          │        4        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P5    │       6        │      3       │        18         │   11    │       9        │        12          │        5        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│ Average │                │              │                   │         │      6.8       │       10.6         │       2.2       │
╘═════════╧════════════════╧══════════════╧═══════════════════╧═════════╧════════════════╧════════════════════╧═════════════════╛

Gantt Chart
[P1:0–2][P2:2–4][P1:4–6][P3:6–7][P2:7–9][P4:9–11][P5:11–13][P1:13–15][P4:15–17][P5:17–18][P1:18–19]
  ```

### Shortest Job Find Non-Preemptive
```java
Scheduling Results: SHORTEST JOB FIRST (Non-Preemptive)
╒═════════╤════════════════╤══════════════╤═══════════════════╤═════════╤════════════════╤════════════════════╤═════════════════╕
│   PID   │  Arrival Time  │  Burst Time  │  Completion Time  │  Start  │  Waiting Time  │  Turn Around Time  │  Response Time  │
╞═════════╪════════════════╪══════════════╪═══════════════════╪═════════╪════════════════╪════════════════════╪═════════════════╡
│   P1    │       0        │      7       │         7         │    0    │       0        │         7          │        0        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P2    │       2        │      4       │        15         │   11    │       3        │         4          │        3        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P3    │       4        │      1       │         8         │    7    │       2        │         5          │        2        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P4    │       5        │      4       │        19         │   15    │       9        │        13          │        9        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P5    │       6        │      3       │        11         │    8    │      10        │        14          │       10        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│ Average │                │              │                   │         │      4.8       │        8.6         │       4.8       │
╘═════════╧════════════════╧══════════════╧═══════════════════╧═════════╧════════════════╧════════════════════╧═════════════════╛

Gantt Chart
[P1:0–7][P3:7–8][P5:8–11][P2:11–15][P4:15–19]
```

## How it works
Since the program runs on a predetermined data, when computing for the completion time:

### For FCFS
```bash
completion_time = previous_burst_time + next_burst_time
```

### For Round Robin with time quantum of 2
```bash
if remaining[pid] <= quantum:
    # process finishes in this slice
    end = time + remaining[pid]       # completion time
    remaining[pid] = 0
    time = end
    # compute metrics using completion time (end)

else:
    # process not yet finished
    remaining[pid] = remaining[pid] - quantum
    time = time + quantum
    end = time                        # partial completion, not final
    # put process back into the queue
```

### For SJF Non-Preemptive
```bash
if process is selected (shortest burst among available):
    start = current_time
    completion_time = current_time + burst_time   # end = time
    current_time = completion_time
    mark process as completed
    # use completion_time to compute turnaround = end - arrival

```

### Computing for Waiting Time, Turn Around Time, Response Time
After solving for completion time, we can now proceed to compute with WT, TAT, and RT:

```java
Formulas for Scheduling Metrics
╒════════════════════╤════════════════════════════════════════╤══════════════════════════════════════════════════════════════════════╕
│      Metric        │                 Formula                │                           Explanation                                │
╞════════════════════╪════════════════════════════════════════╪══════════════════════════════════════════════════════════════════════╡
│ Completion Time    │ CT = time when process finishes        │ The exact clock time when the process completes its last execution.  │
│ (CT)               │                                        │ In non-preemptive (FCFS, SJF): CT = Start + Burst.                   │
│                    │                                        │ In preemptive (RR, SRTF): CT = last end time.                        │
├────────────────────┼────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────┤
│ Turnaround Time    │ TAT = CT - AT                          │ Total time spent in the system from arrival to completion.           │
│ (TAT / T)          │                                        │ Same formula for all algorithms.                                     │
├────────────────────┼────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────┤
│ Waiting Time       │ WT = TAT - BT                          │ Time spent waiting in the ready queue before (and between) runs.     │
│ (WT / W)           │                                        │ In non-preemptive: WT = Start - AT works too.                        │
│                    │                                        │ In preemptive: must use WT = TAT - BT.                               │
├────────────────────┼────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────┤
│ Response Time      │ RT = First Start - AT                  │ Time from arrival until the process first gets CPU time.             │
│ (RT / R)           │                                        │ In FCFS & non-preemptive SJF: RT = WT.                               │
│                    │                                        │ In RR & SRTF: may differ from WT.                                    │
╘════════════════════╧════════════════════════════════════════╧══════════════════════════════════════════════════════════════════════╛


```

### Do note that these results are computed from a predetermined data, it may or may not work on other data

### Enhancements for this project
* To be more dynamic, where the program can run with user input data
* Add visual Gantt chart generation (e.g., ASCII timeline or matplotlib chart) so results are easier to interpret
* Extend support for multiple scheduling algorithms in one run, allowing comparison of FCFS, SJF, SRTF, and RR on the same input set with side-by-side results

  
