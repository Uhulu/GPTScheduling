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

def round_robin_scheduling(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    processes = []
    run_for = 0
    quantum = 0
    
    # Read the input file
    for line in lines:
        line = line.strip()
        if line.startswith("processcount"):
            process_count = int(line.split()[1])
        elif line.startswith("runfor"):
            run_for = int(line.split()[1])
        elif line.startswith("quantum"):
            quantum = int(line.split()[1])
        elif line.startswith("use"):
            scheduling_algorithm = line.split()[1]  # Could be fcfs, sjf, or rr
        elif line.startswith("process"):
            parts = line.split()
            name = parts[2]
            arrival = int(parts[4])
            burst = int(parts[6])
            processes.append(Process(name, arrival, burst))

    output = []

    output.append(f"{process_count} processes")
    if scheduling_algorithm == "rr":
        output.append(f"Using Round-Robin")
        output.append(f"Quantum   {quantum}\n")

    time = 0
    queue = []
    arrived_processes = set()

    while time < run_for or queue:
    # Check for new arrivals before processing any processes

        new_arrivals = [p for p in processes if p.arrival <= time and p.name not in arrived_processes]
        if new_arrivals:
            for p in new_arrivals:
                arrived_processes.add(p.name)
                output.append(f"Time {time:3} : {p.name} arrived")
                queue.append(p)
        
        if queue:
            current_process = queue.pop(0)
        
            if current_process.first_run:
                current_process.first_run = False
                current_process.response_time = time - current_process.arrival

            time_slice = min(quantum, current_process.remaining_time)
            output.append(f"Time {time:3} : {current_process.name} selected (burst {current_process.remaining_time:3})")

            start_time = time  # Remember the start time before processing
            current_process.remaining_time -= time_slice
            time += time_slice
        
            # Check for new arrivals that occur during the time slice
            new_arrivals_during_slice = [p for p in processes if p.arrival > start_time and p.arrival <= time and p.name not in arrived_processes]
            if new_arrivals_during_slice:
                for p in new_arrivals_during_slice:
                    arrived_processes.add(p.name)
                    output.append(f"Time {p.arrival:3} : {p.name} arrived") #wrote myself
                    queue.append(p)

            # Decide if we need to re-add the current process to the queue
            if current_process.remaining_time > 0:
                # Re-add process to the queue if it still needs time
                queue.append(current_process)
            else:
                output.append(f"Time {time:3} : {current_process.name} finished")
                
                current_process.turnaround_time = time - current_process.arrival
                current_process.wait_time = current_process.turnaround_time - current_process.burst
        else:
            # Increment time if idle
            output.append(f"Time {time:3} : Idle")
            time += 1

    
    output.append(f"Finished at time {time}\n")
    
    for p in processes:
        output.append(f"{p.name} wait {p.wait_time:3} turnaround {p.turnaround_time:3} response {p.response_time:3}")
    
    with open('output.out', 'w') as f:
        for line in output:
            f.write(line + '\n')
    
    

# Run the function with your input file
round_robin_scheduling('c5-rr.in')



