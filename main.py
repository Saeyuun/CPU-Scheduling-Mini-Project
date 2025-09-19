import argparse
from algo.fcfs import fcfs
from algo.sjf import sjf
from algo.rr import rr

# Dataset (fixed)
processes = [
    ("P1", 0, 7),
    ("P2", 2, 4),
    ("P3", 4, 1),
    ("P4", 5, 4),
    ("P5", 6, 3),
]

def print_results(name, results, processes):
    print(f"{name}")
    print("Gantt:", "".join(results["gantt"]))
    print("Per-process (W / T / R):")

    # Map PID -> index for waiting/turnaround/response values
    waiting_map = {}
    turnaround_map = {}
    response_map = {}

    if isinstance(results["waiting"], dict):
        waiting_map = results["waiting"]
        turnaround_map = results["turnaround"]
        response_map = results["response"]
    else:
        # when stored as lists in order of input processes
        for i, (pid, _, _) in enumerate(processes):
            waiting_map[pid] = results["waiting"][i]
            turnaround_map[pid] = results["turnaround"][i]
            response_map[pid] = results["response"][i]

    for pid, _, _ in processes:
        w = waiting_map[pid]
        t = turnaround_map[pid]
        r = response_map[pid]
        print(f"{pid}: {w} / {t} / {r}")

    avg_w, avg_t, avg_r = results["avg"]
    print(
        f"Averages: Waiting {avg_w:.1f}, Turnaround {avg_t:.1f}, Response {avg_r:.1f}"
    )
    print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo", type=str.upper, choices=["FCFS", "SJF", "RR"], required=True)
    parser.add_argument("--quantum", type=int, default=2)
    args = parser.parse_args()

    if args.algo == "FCFS":
        results = fcfs(processes)
        print_results("FCFS", results, processes)

    elif args.algo == "SJF":
        results = sjf(processes)
        print_results("SJF (non-preemptive)", results, processes)

    elif args.algo == "RR":
        results = rr(processes, args.quantum)
        print_results(f"Round Robin (q={args.quantum})", results, processes)


if __name__ == "__main__":
    main()
