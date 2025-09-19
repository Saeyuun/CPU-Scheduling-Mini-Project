from collections import deque

def rr(processes, quantum):
    time = 0
    gantt = []
    waiting, turnaround, response = {}, {}, {}
    remaining = {pid: bt for pid, at, bt in processes}
    first_response = {}

    queue = deque()
    processes_sorted = sorted(processes, key=lambda x: x[1])
    i = 0
    n = len(processes)

    while i < n or queue or any(remaining.values()):
        # Add newly arrived processes
        while i < n and processes_sorted[i][1] <= time:
            pid, at, bt = processes_sorted[i]
            queue.append(pid)
            i += 1

        if not queue:
            time = processes_sorted[i][1]
            continue

        pid = queue.popleft()
        at = [p[1] for p in processes if p[0] == pid][0]

        if pid not in first_response:
            first_response[pid] = time - at

        start = time
        slice_time = min(quantum, remaining[pid])
        time += slice_time
        end = time
        gantt.append(f"[{pid}:{start}–{end}]")
        remaining[pid] -= slice_time

        # Add new arrivals during this quantum
        while i < n and processes_sorted[i][1] <= time:
            queue.append(processes_sorted[i][0])
            i += 1

        if remaining[pid] > 0:
            queue.append(pid)
        else:
            waiting[pid] = end - at - [p[2] for p in processes if p[0] == pid][0]
            turnaround[pid] = end - at
            response[pid] = first_response[pid]

    avg_w = sum(waiting.values()) / n
    avg_t = sum(turnaround.values()) / n
    avg_r = sum(response.values()) / n

    return {
        "gantt": gantt,
        "waiting": list(waiting.values()),
        "turnaround": list(turnaround.values()),
        "response": list(response.values()),
        "avg": (avg_w, avg_t, avg_r)
    }
