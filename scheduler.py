import sys


class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.end_time = None
        self.wait_time = 0
        self.turnaround_time = 0
        self.response_time = None

    def __repr__(self):
        return (
            f"Process({self.name}, Arrival: {self.arrival_time}, "
            f"Burst: {self.burst_time}, Remaining: {self.remaining_time})"
        )


def parse_input(filename):
    processes = []
    process_count = None
    run_for = None
    scheduling_algorithm = None
    quantum = None

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found.")
        sys.exit(1)

    for line in lines:
        line = line.strip()
        if line.startswith("processcount"):
            process_count = int(line.split()[1])
        elif line.startswith("runfor"):
            run_for = int(line.split()[1])
        elif line.startswith("use"):
            scheduling_algorithm = line.split()[1]
        elif line.startswith("quantum"):
            quantum = int(line.split()[1])
        elif line.startswith("process"):
            parts = line.split()
            name = parts[2]
            arrival = int(parts[4])
            burst = int(parts[6])
            processes.append(Process(name, arrival, burst))
        elif line.startswith("end"):
            break

    if process_count is None or run_for is None or scheduling_algorithm is None:
        print("Error: Missing parameters.")
        sys.exit(1)

    return processes, run_for, scheduling_algorithm, quantum


def round_robin_scheduling(processes, run_for, quantum):
    output = [
        f"{len(processes)} processes",
        f"Using Round-Robin",
        f"Quantum   {quantum}\n",
    ]

    time = 0
    queue = []
    arrived_processes = set()

    while time < run_for or queue:
        new_arrivals = [
            p
            for p in processes
            if p.arrival_time == time and p.name not in arrived_processes
        ]
        for p in new_arrivals:
            arrived_processes.add(p.name)
            output.append(f"Time {time:3} : {p.name} arrived")
            queue.append(p)

        if queue:
            current_process = queue.pop(0)
            if current_process.start_time is None:
                current_process.start_time = time
                current_process.response_time = time - current_process.arrival_time

            time_slice = min(quantum, current_process.remaining_time)
            output.append(
                f"Time {time:3} : {current_process.name} selected (burst {current_process.remaining_time:3})"
            )
            current_process.remaining_time -= time_slice
            time += time_slice

            for p in processes:
                if (
                    p.arrival_time > current_process.arrival_time
                    and p.arrival_time <= time
                    and p.name not in arrived_processes
                ):
                    arrived_processes.add(p.name)
                    output.append(f"Time {p.arrival_time:3} : {p.name} arrived")
                    queue.append(p)

            if current_process.remaining_time > 0:
                queue.append(current_process)
            else:
                output.append(f"Time {time:3} : {current_process.name} finished")
                current_process.end_time = time
                current_process.turnaround_time = (
                    current_process.end_time - current_process.arrival_time
                )
                current_process.wait_time = (
                    current_process.turnaround_time - current_process.burst_time
                )
        else:
            output.append(f"Time {time:3} : Idle")
            time += 1

    output.append(f"Finished at time  {time}\n")
    for p in processes:
        if p.end_time is not None:
            output.append(
                f"{p.name} wait {p.wait_time:3} turnaround {p.turnaround_time:3} response {p.response_time:3}"
            )
        else:
            output.append(f"{p.name} did not finish")

    return output


def fcfs_scheduling(processes, total_time):
    output = [f"{len(processes)} processes", "Using First-Come First-Served\n"]

    current_time = 0
    waiting_queue = []

    # Sort processes by arrival time
    processes.sort(key=lambda p: p.arrival_time)

    while current_time < total_time:
        # Check for new arrivals at the current time
        for process in processes:
            if process.arrival_time == current_time and process not in waiting_queue:
                output.append(f"Time {current_time:>3} : {process.name} arrived")
                waiting_queue.append(process)

        if waiting_queue:
            current_process = waiting_queue.pop(0)
            if current_process.start_time is None:
                current_process.start_time = current_time
                current_process.response_time = (
                    current_time - current_process.arrival_time
                )

            output.append(
                f"Time {current_time:>3} : {current_process.name} selected (burst {current_process.burst_time:>3})"
            )
            current_time += current_process.burst_time

            if current_time <= total_time:
                # Log finishing the current process
                output[0].append(f"Time {current_time:>3} : {current_process.name} finished")
                output[1].append(f"| {current_time:>3} | `{current_process.name}` | **finished** |")
                current_process.end_time = current_time
                current_process.turnaround_time = (
                    current_process.end_time - current_process.arrival_time
                )
                current_process.wait_time = (
                    current_process.turnaround_time - current_process.burst_time
                )
            else:
                waiting_queue.append(current_process)
                current_time = total_time

            # Check for new arrivals during the process execution
            for process in processes:
                if (
                    process.arrival_time > current_process.start_time
                    and process.arrival_time <= current_time
                    and process not in waiting_queue
                ):
                    output.append(
                        f"Time {process.arrival_time:>3} : {process.name} arrived"
                    )
                    waiting_queue.append(process)
        else:
            output.append(f"Time {current_time:>3} : Idle")
            current_time += 1

    # Handle any remaining idle time until total_time
    while current_time < total_time:
        output.append(f"Time {current_time:>3} : Idle")
        current_time += 1

    output.append(f"Finished at time {current_time}\n")

    # Generate final statistics for each process in alphabetical order
    for p in sorted(processes, key=lambda x: x.name):
        if not waiting_queue.__contains__(p):
            wait_time = p.wait_time if p.wait_time is not None else 0
            turnaround_time = p.turnaround_time if p.turnaround_time is not None else 0
            response_time = p.response_time if p.response_time is not None else 0
            output[0].append(
                f"{p.name} wait {wait_time:>3} turnaround {turnaround_time:>3} response {response_time:>3}"
            )
            output[1].append(
                f"| `{p.name}` | {wait_time:>3} | {turnaround_time:>3} | {response_time:>3} |"
            )
    
    output[1].append("")
    for p in sorted(waiting_queue, key=lambda x: x.name):
        output[0].append(f"{p.name} did not finish")
        output[1].append(f"`{p.name}` _did not finish_")

    return output


def sjf_preemptive_scheduler(processes, total_runtime):

    current_time = 0

    # Timeline where information about each process will be appended to
    timeline = [f"{len(processes)} processes", "Using Preemptive Shortest Job First"]

    # Keep track of the waiting times
    waiting_times = {}

    # Keep track of the turnaround times
    turnaround_times = {}

    # Track the last selected process to detect preemptions
    last_selected_process = None

    # Main loop that runs while there's still running time left
    while current_time < total_runtime:
        available_processes = [
            p
            for p in processes
            if p.arrival_time <= current_time and p.remaining_time > 0
        ]

        # Log arrival of processes at current time (First)
        for p in processes:
            if p.arrival_time == current_time:
                timeline.append(f"Time {current_time:>3} : {p.name} arrived")

        # If a process finished during the last time unit, log its completion (Second)
        if last_selected_process and last_selected_process.remaining_time == 0:
            timeline.append(f"Time {current_time:>3} : {last_selected_process.name} finished")
            turnaround_times[last_selected_process.name] = (
                current_time - last_selected_process.arrival_time
            )
            waiting_times[last_selected_process.name] = (
                turnaround_times[last_selected_process.name] - last_selected_process.burst_time
            )
            last_selected_process = None  # Reset the last selected process

        # If no process is available, the CPU is idle
        if not available_processes:
            timeline.append(f"Time {current_time:>3} : Idle")
            current_time += 1
            continue

        # Select the process with the shortest remaining burst time (Third)
        shortest_job = min(available_processes, key=lambda p: p.remaining_time)

        # Check if this process is different from the last selected process
        if last_selected_process != shortest_job:
            timeline.append(
                f"Time {current_time:>3} : {shortest_job.name} selected "
                f"(burst {shortest_job.remaining_time})"
            )
            last_selected_process = shortest_job

        # Update the response time if it's the first time the process is being selected
        if shortest_job.start_time is None:
            shortest_job.start_time = current_time
            shortest_job.response_time = current_time - shortest_job.arrival_time

        # Execute the selected process for one time unit
        shortest_job.remaining_time -= 1

        # Increment the time unit by 1
        current_time += 1

    # Append the finish time along with the final statistics
    timeline.append(f"Finished at time {current_time}\n")
    for p in processes:
        timeline.append(
            f"{p.name} wait {waiting_times.get(p.name, 0):>3}"
            f" turnaround {turnaround_times.get(p.name, 0):>3}"
            f" response {p.response_time if p.response_time is not None else 0:>3}"
        )

    # Return the contents of the timeline
    return timeline


print("hello")
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: scheduler.py <input file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file.replace(".in", ".out")

    processes, run_for, scheduling_algorithm, quantum = parse_input(input_file)

    if scheduling_algorithm == "rr":
        if quantum is None:
            quantum = 2  # Default quantum for Round Robin
        output = round_robin_scheduling(processes, run_for, quantum)
    elif scheduling_algorithm == "fcfs":
        output = fcfs_scheduling(processes, run_for)
    elif scheduling_algorithm == "sjf":
        output = sjf_preemptive_scheduler(processes, run_for)
    else:
        print("Error: Invalid scheduling algorithm specified.")
        sys.exit(1)

    # Write output to the .out file
    with open(output_file, "w") as f:
        for line in output:
            f.write(line + "\n")

    print(f"Output written to {output_file}")
