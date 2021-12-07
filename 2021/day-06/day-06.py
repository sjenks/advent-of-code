def main():
	filepath = "input.txt"

	with open(filepath) as f:
		lines = f.readlines()
		split = lines[0].split(',')
		times = [int(s) for s in split]
	time_and_cts = [0]*9 #timer counts of 0-8
	print(time_and_cts)
	for time in times:
		print(time)
		time_and_cts[time] = time_and_cts[time] + 1

	i = 0
	while i < 256:
		time_and_cts = time_step(time_and_cts)
		i += 1

	print(time_and_cts)
	print(count_fish(time_and_cts))

# (current time, num at it, started at)
def time_step(tcts):
	next_iter = [0]*9
	for i in range(len(tcts)):
		if i > 0: # has time left, decrease time
			next_iter[i - 1] = next_iter[i - 1] + tcts[i]
		else: #no time left, reset time
			next_iter[6] = next_iter[6] + tcts[i]
			#spawn babies
			next_iter[8] = next_iter[8] + tcts[i]

	return next_iter

def count_fish(time_and_cts):
	total_fish = 0
	for tcts in time_and_cts:
		total_fish += tcts
	return total_fish

if __name__ == "__main__":
	main()