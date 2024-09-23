class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name  # Process name
        self.arrival_time = arrival_time  # Time when process arrives in the queue
        self.burst_time = burst_time  # Time required to complete the process
        self.remaining_time = (
            burst_time  # Remaining burst time (to track time during execution)
        )
        self.start_time = None  # Time when the process starts execution
        self.end_time = None  # Time when the process finishes execution
        self.status = "Waiting"  # Status of the process
        self.wait_time = 0  # Time process waited before starting execution
        self.turnaround_time = 0  # Time from arrival to completion
        self.response_time = (
            None  # Time from arrival to first response (when it starts)
        )

    def __repr__(self):
        return f"Process({self.name}, Arrival: {self.arrival_time}, Burst: {self.burst_time}, Status: {self.status})"


class FIFOQueue:
    def __init__(self):
        self.processes = []  # List of processes to run
        self.current_time = 0  # The simulation clock time

    def enqueue(self, process):
        self.processes.append(process)

    def run(self, total_time):
        print(f"{len(self.processes)} processes")
        print("Using First In First Out (FIFO)")

        # Sort processes by their arrival time for execution
        sorted_processes = sorted(self.processes, key=lambda p: p.arrival_time)

        completed_processes = []
        process_in_execution = None
        idle_since = None

        while self.current_time < total_time:
            # Check if a process has arrived at this time
            arrived_processes = [
                p for p in sorted_processes if p.arrival_time == self.current_time
            ]
            for process in arrived_processes:
                print(f"Time {self.current_time:>3}: {process.name} arrived")

            # If no process is running and processes have arrived, select the next one
            if process_in_execution is None:
                available_processes = [
                    p
                    for p in sorted_processes
                    if p.arrival_time <= self.current_time and p.status == "Waiting"
                ]
                if available_processes:
                    process_in_execution = available_processes[0]
                    process_in_execution.status = "Running"
                    process_in_execution.start_time = self.current_time
                    process_in_execution.response_time = (
                        self.current_time - process_in_execution.arrival_time
                    )
                    print(
                        f"Time {self.current_time:>3}: {process_in_execution.name} selected (burst {process_in_execution.burst_time:>3})"
                    )
                    idle_since = None
                else:
                    # No process ready, system is idle
                    if idle_since is None or idle_since < self.current_time:
                        print(f"Time {self.current_time:>3}: Idle")
                        idle_since = self.current_time

            # If a process is running, decrement its remaining burst time
            if process_in_execution is not None:
                process_in_execution.remaining_time -= 1

                # If the process finishes
                if process_in_execution.remaining_time == 0:
                    process_in_execution.end_time = self.current_time + 1
                    process_in_execution.turnaround_time = (
                        process_in_execution.end_time
                        - process_in_execution.arrival_time
                    )
                    process_in_execution.wait_time = (
                        process_in_execution.start_time
                        - process_in_execution.arrival_time
                    )
                    completed_processes.append(process_in_execution)
                    print(
                        f"Time {self.current_time + 1:>3}: {process_in_execution.name} finished"
                    )
                    process_in_execution = None

            self.current_time += 1

        # Print the completion time
        print(f"Finished at time {total_time}")

        # Print the wait, turnaround, and response times in the order they were added (not completion order)
        for process in self.processes:
            print(
                f"{process.name} wait {process.wait_time:>3} "
                f"turnaround {process.turnaround_time:>3} "
                f"response {process.response_time:>3}"
            )


# Example usage:
queue = FIFOQueue()

# Create processes
process_a = Process("P01", 0, 5)
process_b = Process("P02", 5, 9)
process_c = Process("P03", 9, 3)
process_d = Process("P04", 1, 4)
process_e = Process("P05", 10, 8)
process_f = Process("P06", 23, 4)
process_g = Process("P07", 12, 5)
process_h = Process("P08", 25, 4)
process_i = Process("P09", 30, 7)
process_j = Process("P10", 13, 2)


# Enqueue processes
queue.enqueue(process_a)
queue.enqueue(process_b)
queue.enqueue(process_c)
queue.enqueue(process_d)
queue.enqueue(process_e)
queue.enqueue(process_f)
queue.enqueue(process_g)
queue.enqueue(process_h)
queue.enqueue(process_i)
queue.enqueue(process_j)


queue.run(total_time=55)
