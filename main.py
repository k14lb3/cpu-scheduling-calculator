import os
import operator

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


def cmd_prio(processes):
    pass


def cmd_rr(processes):
    pass


def cmd_sjf(processes):

    processes_sjf = sorted(processes, key=operator.itemgetter(1))

    gen_gantt_chart(processes_sjf)

    processes_total_waiting_time = 0

    for i in range(len(processes_sjf)):
        processes_sjf[i].append(
            processes_sjf[i - 1][1] + processes_sjf[i - 1][2] if i != 0 else 0
        )
    
    for i in range(len(processes_sjf)):
        processes_total_waiting_time += processes_sjf[i][2]

    print("\n\nProcess\t\tBurst Time\tWaiting Time")
    for i in range(len(processes)):
        print(f"P{processes_sjf[i][0]}\t\t{processes_sjf[i][1]}\t\t{processes_sjf[i][2]}")

    print(
        f"\nAverage Waiting Time:\t{processes_total_waiting_time} / {len(processes_sjf)} = {processes_total_waiting_time / len(processes_sjf)}",
        end="",
    )


def cmd_fcfs(processes):
    processes_fcfs = processes

    gen_gantt_chart(processes)

    processes_total_waiting_time = 0

    for i in range(len(processes_fcfs)):
        processes_fcfs[i].append(
            processes_fcfs[i - 1][1] + processes_fcfs[i - 1][2] if i != 0 else 0
        )
    
    for i in range(len(processes_fcfs)):
        processes_total_waiting_time += processes_fcfs[i][2]

    print("\n\nProcess\t\tBurst Time\tWaiting Time")
    for i in range(len(processes)):
        print(f"P{processes_fcfs[i][0]}\t\t{processes_fcfs[i][1]}\t\t{processes_fcfs[i][2]}")

    print(
        f"\nAverage Waiting Time:\t{processes_total_waiting_time} / {len(processes_fcfs)} = {processes_total_waiting_time / len(processes_fcfs)}",
        end="",
    )


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
