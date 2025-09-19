def sjf(processes):
    time = 0
    gantt = []
    waiting, turnaround, response = [], [], []
    completed = set()

    n = len(processes)
    while len(completed) < n:
        # Select available process with shortest burst
        available = [p for p in processes if p[1] <= time and p[0] not in completed]
        if not available:
            time += 1
            continue

        pid, at, bt = min(available, key=lambda x: x[2])
        start = time
        time += bt
        end = time
        completed.add(pid)
        gantt.append(f"[{pid}:{start}–{end}]")

        w = start - at
        t = end - at
        r = start - at
        waiting.append(w)
        turnaround.append(t)
        response.append(r)

    avg_w = sum(waiting) / n
    avg_t = sum(turnaround) / n
    avg_r = sum(response) / n

    return {
        "gantt": gantt,
        "waiting": waiting,
        "turnaround": turnaround,
        "response": response,
        "avg": (avg_w, avg_t, avg_r)
    }
