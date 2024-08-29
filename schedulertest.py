class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name  # Process name
        self.arrival_time = arrival_time  # Time when process arrives in the queue
        self.burst_time = burst_time  # Time required to complete the process
        self.status = (
            "Waiting"  # Status of the process (e.g., 'Waiting', 'Running', 'Completed')
        )

    def __repr__(self):
        return f"Process({self.name}, Arrival: {self.arrival_time}, Burst: {self.burst_time}, Status: {self.status})"


class FIFOQueue:
    def __init__(self):
        # Initialize an empty list to represent the queue
        self.queue = []

    def enqueue(self, process):
        # Add a process to the end of the queue
        self.queue.append(process)

    def dequeue(self):
        # Remove and return the process at the front of the queue
        # Check if the queue is empty before dequeuing
        if not self.is_empty():
            process = self.queue.pop(0)
            process.status = "Completed"
            return process
        else:
            raise IndexError("Dequeue from an empty queue")

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def peek(self):
        # Return the process at the front of the queue without removing it
        # Check if the queue is empty before peeking
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Peek from an empty queue")

    def size(self):
        # Return the number of processes in the queue
        return len(self.queue)

    def update_status(self, process_name, new_status):
        # Update the status of a specific process by name
        for process in self.queue:
            if process.name == process_name:
                process.status = new_status
                return
        raise ValueError(f"Process with name {process_name} not found")


# Example usage:
queue = FIFOQueue()

# Create processes
process_a = Process("A", 0, 5)
process_b = Process("B", 1, 4)
process_c = Process("C", 4, 2)

# Enqueue processes
queue.enqueue(process_a)
queue.enqueue(process_b)
queue.enqueue(process_c)

# Dequeue a process and print its details
dequeued_process = queue.dequeue()
print(dequeued_process)  # Output: Process(A, Arrival: 0, Burst: 5, Status: Completed)

# Peek at the next process in the queue
print(queue.peek())  # Output: Process(B, Arrival: 1, Burst: 4, Status: Waiting)

# Update process status
queue.update_status("B", "Running")
print(queue.peek())  # Output: Process(B, Arrival: 1, Burst: 4, Status: Running)
