
class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.status = "Waiting"
        self.remaining_burst_time = burst_time
        self.selected = False

    def __str__(self):
        return f"Process {self.name}: Arrival Time={self.arrival_time}, Burst Time={self.burst_time}, Status={self.status}"



# Pre-emptive SJF Function
def sjf_preemptive_scheduler(processes, total_runtime):
    current_time = 0
    executed_processes = []
    response_times = {}
    waiting_times = {}
    turnaround_times = {}
    timeline = []

    timeline.append(f"{len(processes)} processes")
    timeline.append("Using Preemptive Shortest Job First")

    # Returns the process with the shortest remaining burst time
    def select_shortest_job(available_processes):
        return min(available_processes, key=lambda x: x.remaining_burst_time)

    # Checks if any processes are remaining
    def has_remaining_processes():
        return any(process.status != "finished" for process in processes)

    # Main scheduling loop
    while current_time < total_runtime or has_remaining_processes():

        # Check for arriving processes
        for process in processes:
            if process.arrival_time == current_time and process.status == "Waiting":
                timeline.append(f"Time {current_time} : {process.name} arrived")

         # Filter processes that have arrived by current time
        eligible_processes = [p for p in processes if p.arrival_time <= current_time and p.status == "Waiting"]

        if not eligible_processes:
            timeline.append(f"Time {current_time} : Idle")
            current_time += 1
            continue

        # Select the process with the shortest remaining burst time
        shortest_job = select_shortest_job(eligible_processes)

        # Output the selected process if it's the first time it's being selected
        if not shortest_job.selected:
            timeline.append(f"Time {current_time} : {shortest_job.name} selected (burst {shortest_job.burst_time})")
            shortest_job.selected = True

        # Update response time for the first occurrence of the process
        if shortest_job.name not in response_times:
            response_times[shortest_job.name] = current_time - shortest_job.arrival_time

        # Process the execution for 1 time unit
        shortest_job.remaining_burst_time -= 1

        # Check if the process has finished executing
        if shortest_job.remaining_burst_time == 0:
            shortest_job.status = "finished"
            executed_processes.append(shortest_job.name)
            timeline.append(f"Time {current_time + 1} : {shortest_job.name} finished")

            # Calculate turnaround time and waiting time
            waiting_times[shortest_job.name] = current_time - shortest_job.arrival_time - shortest_job.burst_time + 1
            turnaround_times[shortest_job.name] = current_time - shortest_job.arrival_time + 1

        # Move time forward by 1 unit
        current_time += 1

    # Print final time
    timeline.append(f"Finished at time {total_runtime}")

    # Return all the recorded details
    return {
        "timeline": timeline,
        "response_times": response_times,
        "waiting_times": waiting_times,
        "turnaround_times": turnaround_times,
        "executed_processes": executed_processes
    }


# Example usage
processes = [
    Process("A", 0, 5),
    Process("B", 1, 4),
    Process("C", 4, 2)
]
total_runtime = 20
result = sjf_preemptive_scheduler(processes, total_runtime)

# Print the timeline of events
for event in result["timeline"]:
    print(event)