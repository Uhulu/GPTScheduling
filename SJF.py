class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_burst_time = burst_time
        self.status = 'waiting'
        self.selected = False
        self.response_time = None
        self.finish_time = None

def sjf_scheduler(processes, total_runtime):
    current_time = 0
    executed_processes = []
    response_times = {}
    waiting_times = {}
    turnaround_times = {}
    timeline = []

    # Sort processes by arrival time initially
    processes.sort(key=lambda p: p.arrival_time)

    timeline.append(f"{len(processes)} processes")
    timeline.append("Using Preemptive Shortest Job First")

    # Keep track of which processes have been announced
    announced_processes = set()

    while current_time < total_runtime:
        # Check if any process has arrived and log their arrival
        for process in processes:
            if process.arrival_time == current_time and process.name not in announced_processes:
                timeline.append(f"Time {current_time} : {process.name} arrived")
                announced_processes.add(process.name)
        
        # Find all processes that have arrived by the current time
        arrived_processes = [p for p in processes if p.arrival_time <= current_time and p.remaining_burst_time > 0]

        if arrived_processes:
            # Find the process with the shortest remaining burst time
            current_process = min(arrived_processes, key=lambda p: p.remaining_burst_time)

            if not current_process.selected:
                current_process.selected = True
                current_process.response_time = current_time - current_process.arrival_time
                timeline.append(f"Time {current_time} : {current_process.name} selected (burst {current_process.burst_time})")
            
            # Calculate execution time
            execution_time = min(current_process.remaining_burst_time, total_runtime - current_time)
            current_time += execution_time
            current_process.remaining_burst_time -= execution_time
            
            if current_process.remaining_burst_time == 0:
                current_process.status = 'finished'
                current_process.finish_time = current_time
                turnaround_times[current_process.name] = current_time - current_process.arrival_time
                timeline.append(f"Time {current_time} : {current_process.name} finished")
                executed_processes.append(current_process.name)
                
            # Update waiting time for remaining processes
            for p in processes:
                if p != current_process and p.arrival_time <= current_time and p.remaining_burst_time > 0:
                    waiting_times[p.name] = waiting_times.get(p.name, 0) + execution_time
            
        else:
            timeline.append(f"Time {current_time} : Idle")
            current_time += 1

    # Handle any processes that didn't finish
    unfinished_processes = [p for p in processes if p.name not in executed_processes]
    for p in unfinished_processes:
        timeline.append(f"{p.name} did not finish")
    
    # Print final time
    timeline.append(f"Finished at time {total_runtime}")

    # Final metrics reporting
    for p in processes:
        if p.name in response_times:
            wait_time = waiting_times.get(p.name, 0) - (p.burst_time - response_times[p.name])
            turnaround_time = turnaround_times.get(p.name, 0)
            response_time = response_times.get(p.name, 0)
            timeline.append(f"{p.name} wait {wait_time} turnaround {turnaround_time} response {response_time}")
    
    return timeline

# Example usage:
p1 = Process(name='A', arrival_time=0, burst_time=5)
p2 = Process(name='B', arrival_time=1, burst_time=4)
p3 = Process(name='C', arrival_time=4, burst_time=2)

processes = [p1, p2, p3]
total_runtime = 20
timeline = sjf_scheduler(processes, total_runtime)

for event in timeline:
    print(event)
