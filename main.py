import os

CMD_FCFS = "fcfs"
CMD_SJF = "sjf"
CMD_RR = "rr"
CMD_PRIO = "prio"
CMD_DISPROC = "disproc"
CMD_PROC = "proc"
CMD_HELP = "help"
CMD_CLEAR = "clear"
COMMANDS = {
    CMD_FCFS: "Apply First-Come First-Served Scheduling.",
    CMD_SJF: "Apply Shortest-Job-First Scheduling.",
    CMD_RR: "Apply Round Robin Scheduling.",
    CMD_PRIO: "Apply Priority Scheduling.",
    CMD_DISPROC: "Display the processes.",
    CMD_PROC: "Input or replace current processes.",
    CMD_HELP: "Display commands.",
    CMD_CLEAR: "Clears the terminal.",
}


def cmd_prio(processes):
    pass


def cmd_rr(processes):
    pass


def cmd_sjf(processes):
    pass


def cmd_fcfs(processes):
    pass


def cmd_disproc(processes):
    print("\nProcess\t\tBurst Time")
    for i in range(len(processes)):
        print(f"P{i+1}\t\t{processes[i]}")


def cmd_proc(processes):
    process_count = int(input("\nInput number of processes: "))

    for i in range(process_count):
        processes.append(int(input(f"P{i + 1} Burst Time: ")))

    cmd_disproc(processes)


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
        elif cmd == CMD_DISPROC:
            if len(processes) != 0:
                cmd_disproc(processes)
            else:
                print("Input processes first!")
        elif cmd == CMD_HELP:
            cmd_help()
        elif cmd == CMD_PROC:
            cmd_proc(processes)
        elif cmd == CMD_CLEAR:
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print(f"Command not found: {cmd}")


if __name__ == "__main__":
    main()
