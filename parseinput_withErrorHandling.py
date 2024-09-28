import sys

class Process:
    def __init__(self, name, arrival, burst):
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.remaining_time = burst
        self.wait_time = 0
        self.turnaround_time = 0
        self.response_time = -1
        self.first_run = True

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
                    raise ValueError("Missing process count.")
                try:
                    process_count = int(parts[1])
                    if process_count <= 0:
                        raise ValueError("Process count must be a positive integer.")
                except ValueError:
                    raise ValueError(f"Invalid process count: {parts[1]}")
            elif line.startswith("runfor"):
                run_for = int(line.split()[1])
                if run_for <= 0:
                    raise ValueError("Run time must be a positive integer.")
            elif line.startswith("use"):
                parts = line.split()
                if len(parts) < 2:
                    raise ValueError("Missing scheduling algorithm after 'use'.")
                scheduling_algorithm = parts[1].lower()
                if scheduling_algorithm not in ["fcfs", "sjf", "rr"]:
                    raise ValueError(f"Invalid scheduling algorithm: {scheduling_algorithm}. Use 'fcfs', 'sjf', or 'rr'.")
            elif line.startswith("quantum"):
                quantum = int(line.split()[1])
                if quantum <= 0:
                    raise ValueError("Quantum time must be a positive integer.")
            elif line.startswith("process"):
                parts = line.split()
                if len(parts) != 7 or parts[1] != "name" or parts[3] != "arrival" or parts[5] != "burst":
                    raise ValueError(f"Malformed process line: {line}")
                name = parts[2]
                arrival = int(parts[4])
                burst = int(parts[6])
                if arrival < 0 or burst <= 0:
                    raise ValueError(f"Invalid arrival or burst time for process {name}.")
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



def main():
    # Check if the filename is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python scheduler.py <input file>")
        sys.exit(1)

    # Get the filename from the command-line arguments
    filename = sys.argv[1]

    # Call the parse_input function to parse the input file
    processes, run_for, scheduling_algorithm, quantum = parse_input(filename)

    # Print out the parsed information
    print(f"Scheduling algorithm: {scheduling_algorithm}")
    print(f"Run for: {run_for} time units")
    if scheduling_algorithm == "rr":
        print(f"Quantum: {quantum} time units")

    print(f"Processes ({len(processes)}):")
    for process in processes:
        print(f"  Process {process.name}: Arrival = {process.arrival}, Burst = {process.burst}")

if __name__ == "__main__":
    main()
