def read_input_file(filename):
    processes = []
    process_count = 0
    run_time = 0
    scheduling_algorithm = None

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("processcount"):
                process_count = int(line.split()[1])
            elif line.startswith("runfor"):
                run_time = int(line.split()[1])
            elif line.startswith("use"):
                scheduling_algorithm = line.split()[1]
            elif line.startswith("process"):
                # Extract process details
                parts = line.split()
                name = parts[2]
                arrival_time = parts[4]
                burst_time = parts[6]
                # Create a Process object
                process = Process(name, arrival_time, burst_time)
                processes.append(process)
            elif line == "end":
                break

    return process_count, run_time, scheduling_algorithm, processes
