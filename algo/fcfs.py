def fcfs(processes):
    time = 0
    gantt = []
    waiting, turnaround, response = [], [], []

    for pid, at, bt in processes:
        if time < at:
            time = at
        start = time
        time += bt
        end = time
        gantt.append(f"[{pid}:{start}–{end}]")
        
        w = start - at
        t = end - at
        r = start - at
        waiting.append(w)
        turnaround.append(t)
        response.append(r)

    avg_w = sum(waiting) / len(waiting)
    avg_t = sum(turnaround) / len(turnaround)
    avg_r = sum(response) / len(response)

    return {
        "gantt": gantt,
        "waiting": waiting,
        "turnaround": turnaround,
        "response": response,
        "avg": (avg_w, avg_t, avg_r)
    }
