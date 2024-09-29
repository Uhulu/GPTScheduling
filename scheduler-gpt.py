# Matthew Itskovich
# Luke Knowles
# Julian Nutovits
# Jesuel Rosado Arroyo
# Elizabeth Teter

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

    # Error handling for missing input file argument
    if not filename:
        print("Error: No input file provided.")
        sys.exit(1)

    # Error handling for file not found
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found.")
        sys.exit(1)


    # Parse the file
    try:

        for line in lines:
            line = line.strip()

            if line.startswith("processcount"):

               parts = line.split()
               if len(parts) < 2:
                    raise ValueError("Missing parameter process count.")
               try:
                    process_count = int(parts[1])
                    if process_count <= 0:
                        raise ValueError("Process count must be a positive integer.")
               except ValueError:
                    raise ValueError(f"Missing parameter process count.")

            elif line.startswith("runfor"):

               parts = line.split()
               if len(parts) < 2:
                    raise ValueError("Missing parameter run for.")

               try:
                    run_for = int(line.split()[1])
                    if run_for <= 0:
                        raise ValueError("Run time must be a positive integer.")
               except ValueError:
                    raise ValueError(f"Missing parameter run for.")

            elif line.startswith("use"):

                 parts = line.split()
                 if len(parts) < 2:
                    raise ValueError("Missing scheduling algorithm after 'use'.")
                 scheduling_algorithm = parts[1].lower()
                 if scheduling_algorithm not in ["fcfs", "sjf", "rr"]:
                    raise ValueError(f"Invalid scheduling algorithm: {scheduling_algorithm}. Use 'fcfs', 'sjf', or 'rr'.")
            

            elif line.startswith("quantum"):

                parts = line.split()
                if len(parts) < 2:
                    raise ValueError("Missing parameter quantum.")
                try:
                    quantum = int(line.split()[1])
                    if quantum <= 0:
                        raise ValueError("Quantum must be a positive integer.")
                except ValueError:
                    raise ValueError(f"Missing parameter quantum.")


            elif line.startswith("process"):

                parts = line.split()
                if len(parts) != 7 or parts[1] != "name" or parts[3] != "arrival" or parts[5] != "burst":
                    raise ValueError(f"Malformed process information.")
                name = parts[2]
                arrival = int(parts[4])
                burst = int(parts[6])
                if arrival < 0 or burst <= 0:
                    raise ValueError(f"Malformed process information.")
                processes.append(Process(name, arrival, burst))

            elif line.startswith("end"):
                break

    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Check if all required parameters are present
    if process_count is None or run_for is None or scheduling_algorithm is None:
        print("Error: Missing required parameters (processcount, runfor, use).")
        sys.exit(1)

    if scheduling_algorithm == "rr" and quantum is None:
        print("Error: Missing quantum for round-robin scheduling.")
        sys.exit(1)

    if len(processes) != process_count:
        print(f"Error: Expected {process_count} processes, but found {len(processes)}.")
        sys.exit(1)

    return processes, run_for, scheduling_algorithm, quantum


def round_robin_scheduling(processes, run_for, quantum):
    # Initialize two separate outputs: one for a simple output format, the other for a Markdown format
    output = [[
        f"{len(processes)} processes",                # Number of processes
        f"Using Round-Robin",                         # Indicates Round-Robin scheduling is being used
        f"Quantum   {quantum}\n",                     # Time slice (quantum) for Round-Robin
    ],
    [
        f"**{len(processes)}** processes  ",           # Markdown: Number of processes (bold formatting)
        f"Using **Round-Robin**  ",                   # Markdown: Scheduling algorithm being used (bold formatting)
        f"Quantum   **{quantum}**\n",                 # Markdown: Time slice (quantum) for Round-Robin (bold formatting)
        "## Timeline",                                # Markdown: Section header for timeline
        "| **Time** | **Process** | **Action** |",    # Markdown: Table header for time, process, and action
        "|:-:|:-:|:-:|"                               # Markdown: Table alignment for center-aligned columns
    ]]

    time = 0                                          # Global time counter
    queue = []                                        # Queue to hold processes ready to run
    arrived_processes = set()                         # Set to track which processes have arrived

    # Main loop runs while the time is less than the total simulation time
    while time < run_for:
        # Check for new arrivals at the current time
        new_arrivals = [
            p
            for p in processes
            if p.arrival_time == time and p.name not in arrived_processes
        ]
        # Add new arrivals to the queue and mark them as arrived
        for p in new_arrivals:
            arrived_processes.add(p.name)
            output[0].append(f"Time {time:3} : {p.name} arrived")
            output[1].append(f"| {time:3} | `{p.name}` | arrived |")
            queue.append(p)

        if queue:
            current_process = queue.pop(0)            # Get the first process in the queue
            if current_process.start_time is None:    # If the process is running for the first time
                current_process.start_time = time
                current_process.response_time = time - current_process.arrival_time

            # Calculate the time slice (quantum) or remaining burst time, whichever is smaller
            time_slice = min(quantum, current_process.remaining_time)
            output[0].append(
                f"Time {time:3} : {current_process.name} selected (burst {current_process.remaining_time:3})"
            )
            output[1].append(
                f"| {time:3} | `{current_process.name}` | selected (burst {current_process.remaining_time:3}) |"
            )
            current_process.remaining_time -= time_slice  # Decrease the remaining time by the time slice
            time += time_slice                            # Advance the global time by the time slice

            # Check for new arrivals during the time slice
            for p in processes:
                if (
                    p.arrival_time > current_process.arrival_time
                    and p.arrival_time <= time
                    and p.name not in arrived_processes
                ):
                    arrived_processes.add(p.name)
                    output[0].append(f"Time {p.arrival_time:3} : {p.name} arrived")
                    output[1].append(f"| {p.arrival_time:3} | `{p.name}` | arrived |")
                    queue.append(p)

            if current_process.remaining_time > 0:     # If the process still has remaining burst time
                queue.append(current_process)          # Re-add it to the end of the queue
            else:
                output[0].append(f"Time {time:3} : {current_process.name} finished")
                output[1].append(f"| {time:3} | `{current_process.name}` | **finished** |")
                current_process.end_time = time        # Mark the process as finished
                # Calculate turnaround time and wait time
                current_process.turnaround_time = (
                    current_process.end_time - current_process.arrival_time
                )
                current_process.wait_time = (
                    current_process.turnaround_time - current_process.burst_time
                )
        else:
            # If there are no processes in the queue, the system is idle
            output[0].append(f"Time {time:3} : Idle")
            output[1].append(f"| {time:3} | N/A | Idle |")
            time += 1  # Increment the global time when idle

    # After the scheduling ends
    output[0].append(f"Finished at time  {time}\n")
    output[1].append(f"\n**Finished at time  {time}**\n")
    output[1].append("## Metrics\n| **Process** | **Wait** | **Turnaround** | **Response** |\n|:-:|:-:|:-:|:-:|")

    unfinished = []  # To track processes that did not finish
    # Output metrics for each process
    for p in processes:
        if p.end_time is not None:
            # Add the process's wait, turnaround, and response times to the output
            output[0].append(
                f"{p.name} wait {p.wait_time:3} turnaround {p.turnaround_time:3} response {p.response_time:3}"
            )
            output[1].append(
                f"| `{p.name}` | {p.wait_time:3} | {p.turnaround_time:3} | {p.response_time:3} |"
            )
        else:
            # If the process did not finish, note this in the output
            output[0].append(f"{p.name} did not finish")
            unfinished.append(f"`{p.name}` _did not finish_")

    output[1].append("")  # Add an empty line before unfinished processes
    for p in unfinished:
        output[1].append(p)  # Append unfinished processes to the markdown output

    return output  # Return both text and markdown outputs


def fcfs_scheduling(processes, total_time):
    output = [[f"{len(processes)} processes", "Using First-Come First-Served\n"],
              [f"**{len(processes)}** processes  ", "Using **First-Come First-Served**\n",
               "## Timeline", "| **Time** | **Process** | **Action** |", "|:-:|:-:|:-:|"]]

    current_time = 0
    waiting_queue = []

    # Sort processes by arrival time
    processes.sort(key=lambda p: p.arrival_time)

    while current_time < total_time:
        # Check for new arrivals at the current time
        for process in processes:
            if process.arrival_time == current_time and process not in waiting_queue:
                output[0].append(f"Time {current_time:>3} : {process.name} arrived")
                output[1].append(f"| {current_time:>3} | `{process.name}` | arrived |")
                waiting_queue.append(process)

        if waiting_queue:
            current_process = waiting_queue.pop(0)
            if current_process.start_time is None:
                current_process.start_time = current_time
                current_process.response_time = (
                    current_time - current_process.arrival_time
                )

            output[0].append(
                f"Time {current_time:>3} : {current_process.name} selected (burst {current_process.burst_time:>3})"
            )
            output[1].append(
                f"| {current_time:>3} | `{current_process.name}` | selected (burst {current_process.burst_time:>3}) |"
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
                    output[0].append(
                        f"Time {process.arrival_time:>3} : {process.name} arrived"
                    )
                    output[1].append(
                        f"| {process.arrival_time:>3} | `{process.name}` | arrived |"
                    )
                    waiting_queue.append(process)
        else:
            output[0].append(f"Time {current_time:>3} : Idle")
            output[1].append(f"| {current_time:>3} | N/A | Idle |")
            current_time += 1

    # Handle any remaining idle time until total_time
    while current_time < total_time:
        output[0].append(f"Time {current_time:>3} : Idle")
        output[1].append(f"| {current_time:>3} | N/A | Idle |")
        current_time += 1

    output[0].append(f"Finished at time {current_time}\n")
    output[1].append(f"\n**Finished at time {current_time}**\n")
    output[1].append("## Metrics\n| **Process** | **Wait** | **Turnaround** | **Response** |\n|:-:|:-:|:-:|:-:|")

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
    timeline = [[f"{len(processes)} processes", "Using Preemptive Shortest Job First"],
                [f"**{len(processes)}** processes  ", "Using **Preemptive Shortest Job First**",
                "## Timeline", "| **Time** | **Process** | **Action** |", "|:-:|:-:|:-:|"]]

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
                timeline[0].append(f"Time {current_time:>3} : {p.name} arrived")
                timeline[1].append(f"| {current_time:>3} | `{p.name}` | arrived |")

        # If a process finished during the last time unit, log its completion (Second)
        if last_selected_process and last_selected_process.remaining_time == 0:
            timeline[0].append(f"Time {current_time:>3} : {last_selected_process.name} finished")
            timeline[1].append(f"| {current_time:>3} | `{last_selected_process.name}` | **finished** |")
            turnaround_times[last_selected_process.name] = (
                current_time - last_selected_process.arrival_time
            )
            waiting_times[last_selected_process.name] = (
                turnaround_times[last_selected_process.name] - last_selected_process.burst_time
            )
            last_selected_process = None  # Reset the last selected process

        # If no process is available, the CPU is idle
        if not available_processes:
            timeline[0].append(f"Time {current_time:>3} : Idle")
            timeline[1].append(f"| {current_time:>3} | N/A | Idle |")
            current_time += 1
            continue

        # Select the process with the shortest remaining burst time (Third)
        shortest_job = min(available_processes, key=lambda p: p.remaining_time)

        # Check if this process is different from the last selected process
        if last_selected_process != shortest_job:
            timeline[0].append(
                f"Time {current_time:>3} : {shortest_job.name} selected "
                f"(burst {shortest_job.remaining_time})"
            )
            timeline[1].append(
                f"| {current_time:>3} | `{shortest_job.name}` | selected "
                f"(burst {shortest_job.remaining_time}) |"
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

    # Append the finish time
    timeline[0].append(f"Finished at time {current_time}\n")
    timeline[1].append(f"\n**Finished at time {current_time}**\n")
    timeline[1].append("## Metrics\n| **Process** | **Wait** | **Turnaround** | **Response** |\n|:-:|:-:|:-:|:-:|")
    
    unfinished_processes = [p for p in processes if p.remaining_time > 0]

    # Append the final metrics
    for p in processes:
        if p not in unfinished_processes:
            timeline[0].append(
                f"{p.name} wait {waiting_times.get(p.name, 0):>3}"
                f" turnaround {turnaround_times.get(p.name, 0):>3}"
                f" response {p.response_time if p.response_time is not None else 0:>3}"
            )
            timeline[1].append(
                f"| `{p.name}` | {waiting_times.get(p.name, 0):>3}"
                f" | {turnaround_times.get(p.name, 0):>3}"
                f" | {p.response_time if p.response_time is not None else 0:>3} |"
            )
        
    # Append processes that didn't finish
    timeline[1].append("")
    if unfinished_processes:
        for p in unfinished_processes:
            timeline[0].append(f"{p.name} did not finish")
            timeline[1].append(f"`{p.name}` _did not finish_")

    # Return the contents of the timeline
    return timeline


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: scheduler-gpt.py <input file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file.replace(".in", ".out")
    output_file_md = input_file.replace(".in", ".md")

    processes, run_for, scheduling_algorithm, quantum = parse_input(input_file)

    if scheduling_algorithm == "rr":
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
        for line in output[0]:
            f.write(line + "\n")
    
    # Write output to the .md file
    with open(output_file_md, "w") as f:
        for line in output[1]:
            f.write(line + "\n")

    print(f"Output written to {output_file} and {output_file_md}")
