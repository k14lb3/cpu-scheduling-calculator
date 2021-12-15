import os
from math import ceil
import copy

CMD_FCFS = "fcfs"
CMD_SJF = "sjf"
CMD_RR = "rr"
CMD_PRIO = "prio"
CMD_PROC = "proc"
CMD_DISPROC = "disproc"
CMD_HELP = "help"
CMD_CLEAR = "clear"
COMMANDS = {
    CMD_FCFS: "Apply First-Come First-Served Scheduling.",
    CMD_SJF: "Apply Shortest-Job-First Scheduling.",
    CMD_RR: "Apply Round Robin Scheduling.",
    CMD_PRIO: "Apply Priority Scheduling.",
    CMD_PROC: "Input or replace current processes.",
    CMD_DISPROC: "Display the processes.",
    CMD_HELP: "Display commands.",
    CMD_CLEAR: "Clears the terminal.",
}


def gen_gantt_chart(processes):

    # Top Border
    for i in range(len(processes)):
        print(f"--{'-' if processes[i][0] < 10 else '--'}", end="")
        for _ in range(processes[i][1]):
            print("-", end="")
        print("-", end="")
    print("-")

    # Process Number Labels
    for i in range(len(processes)):
        print(f"| P{processes[i][0]}", end="")
        for _ in range(processes[i][1]):
            print(" ", end="")
    print("|")

    # Bottom Border
    for i in range(len(processes)):
        print(f"--{'-' if processes[i][0] < 10 else '--'}", end="")
        for _ in range(processes[i][1]):
            print("-", end="")
        print("-", end="")
    print("-")

    # Waiting Time Labels
    total_time = 0

    print("0", end="")
    for i in range(len(processes)):
        total_time += processes[i][1]
        print(f"  {' ' if processes[i][0] < 10 else '  '}", end="")
        for j in range(processes[i][1]):
            print(" ", end="")
            if j == processes[i][1] - 1:
                if total_time - processes[i - 1][1] > 9:
                    print("\b", end="")
                print(f"{total_time}", end="")


def get_average_waiting_time(processes):
    processes.sort(key=lambda p: p[0])

    processes_total_waiting_time = 0

    for i in range(len(processes)):
        processes_total_waiting_time += processes[i][2]

    print(
        f"\n\nProcess\t\tBurst Time\tWaiting Time\t{'Priority' if len(processes[0]) == 4 else ''}",
    )

    for i in range(len(processes)):
        print(
            f"P{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{processes[i][3] if len(processes[0]) == 4 else ''}"
        )

    print(
        f"\n\tAverage Waiting Time:\t{processes_total_waiting_time} / {len(processes)} = {processes_total_waiting_time / len(processes)}",
    )


def cmd_prio(processes):
    processes_prio = copy.deepcopy(processes)

    print("\n# Lower number = Higher priority")

    for i in range(len(processes_prio)):

        while True:
            priority = int(input(f"P{processes_prio[i][0]} Priority: "))

            if priority > 0:
                break

            print("Invalid input.")

        processes_prio[i].extend([0, priority])

    processes_prio.sort(key=lambda p: p[3])

    gen_gantt_chart(processes_prio)

    for i in range(len(processes_prio)):
        processes_prio[i][2] = (
            processes_prio[i - 1][1] + processes_prio[i - 1][2] if i != 0 else 0
        )

    get_average_waiting_time(processes_prio)


def cmd_rr(processes):

    processes_rr = copy.deepcopy(processes)
    burst_times = [process[1] for process in processes_rr]
    processes_rr_temp = []

    time_quantum = 1

    while True:
        time_quantum = int(input(f"Time Quantum: "))

        if time_quantum > 0:
            break

        print("Invalid input.")

    # Gets the number of iterations by getting the
    # largest burst time and dividing it to the given time quantum.
    iterations = ceil(max(burst_times) / time_quantum)

    for _ in range(iterations):
        # Iterates through all the processes
        for i in range(len(processes_rr)):
            # Excludes the processes that already finished executing.
            if burst_times[i] != 0:
                if burst_times[i] >= time_quantum:
                    burst_time = time_quantum
                    burst_times[i] -= burst_time
                else:
                    burst_time = burst_times[i]
                    burst_times[i] = 0

                processes_rr_temp.append([processes_rr[i][0], burst_time])

    gen_gantt_chart(processes_rr_temp)

    for i in range(len(processes_rr_temp)):
        processes_rr_temp[i].append(
            processes_rr_temp[i - 1][1] + processes_rr_temp[i - 1][2] if i != 0 else 0
        )

    for i in range(len(processes_rr)):
        waiting_time = 0
        encounter = 0
        process_prev = None
        # Iterates through the created sequece
        # which whill also be shown in the gantt chart
        for j in range(len(processes_rr_temp)):
            # Determines if the process that the cursor is currently in
            # is the one that we are calculating the waiting time for.
            if processes_rr_temp[j][0] == processes_rr[i][0]:
                # Determines if the process is its first execution. 
                if encounter != 0:
                    # Gets the time gap between the n and n+1 process
                    # Time gap = Current n process Waiting Time -
                    #           (Previous n process Waiting Time +
                    #           Previous n process Burst Time)
                    waiting_time += processes_rr_temp[j][2] - (
                        process_prev[1] + process_prev[2]
                    )
                else:
                    waiting_time += processes_rr_temp[j][2]
                    encounter += 1

                process_prev = processes_rr_temp[j]

        processes_rr[i].append(waiting_time)

    get_average_waiting_time(processes_rr)



def cmd_sjf(processes):
    processes_sjf = copy.deepcopy(processes)

    processes_sjf.sort(key=lambda p: p[1])

    gen_gantt_chart(processes_sjf)

    for i in range(len(processes_sjf)):
        processes_sjf[i].append(
            processes_sjf[i - 1][1] + processes_sjf[i - 1][2] if i != 0 else 0
        )

    get_average_waiting_time(processes_sjf)


def cmd_fcfs(processes):
    processes_fcfs = copy.deepcopy(processes)

    gen_gantt_chart(processes_fcfs)

    for i in range(len(processes_fcfs)):
        processes_fcfs[i].append(
            processes_fcfs[i - 1][1] + processes_fcfs[i - 1][2] if i != 0 else 0
        )

    get_average_waiting_time(processes_fcfs)


def cmd_proc(processes):
    processes.clear()

    process_count = int(input("\nInput number of processes: "))

    for i in range(process_count):
        processes.append([i + 1, int(input(f"P{i + 1} Burst Time: "))])

    cmd_disproc(processes)


def cmd_disproc(processes):
    print("\nProcess\t\tBurst Time")
    for i in range(len(processes)):
        print(f"P{processes[i][0]}\t\t{processes[i][1]}")


def cmd_help():
    print("\nCommands:")
    for cmd, func in COMMANDS.items():
        print(f"{cmd}\t-\t{func}")


def main():
    cmd_help()

    processes = []

    while True:

        cmd = input("\n➡ ")

        if cmd == CMD_FCFS:
            if len(processes) != 0:
                cmd_fcfs(processes)
            else:
                print("Input processes first!")
        elif cmd == CMD_SJF:
            if len(processes) != 0:
                cmd_sjf(processes)
            else:
                print("Input processes first!")
        elif cmd == CMD_RR:
            if len(processes) != 0:
                cmd_rr(processes)
            else:
                print("Input processes first!")
        elif cmd == CMD_PRIO:
            if len(processes) != 0:
                cmd_prio(processes)
            else:
                print("Input processes first!")
        elif cmd == CMD_PROC:
            cmd_proc(processes)
        elif cmd == CMD_DISPROC:
            if len(processes) != 0:
                cmd_disproc(processes)
            else:
                print("Input processes first!")
        elif cmd == CMD_HELP:
            cmd_help()
        elif cmd == CMD_CLEAR:
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print(f"Command not found: {cmd}")


if __name__ == "__main__":
    main()
