#  initialize processes
processes = [('P1', 50, 0), ('P2', 20, 20), ('P3', 100, 40), ('P4', 40, 60)]

# sort the processes by arrival time

processes.sort(key=lambda x: x[2])

# initialize current time and waiting time
current_time = 0
waiting_times = []

for process in processes:
	name, burst_time, arrival_time = process
	if current_time < arrival_time:
		current_time = arrival_time
	waiting_time = current_time - arrival_time
	waiting_times.append(waiting_time)
	current_time += burst_time
	print(f'Gant Chat {name} runs from {current_time - burst_time} to {current_time}')

# Find the average of waiting time 
average_wait_time = sum(waiting_times) / len(waiting_times)

print(f'The average of waiting_time is: {average_wait_time:.2f} ms')
