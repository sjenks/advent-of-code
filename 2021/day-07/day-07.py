def main():
	filepath = "input.txt"

	with open(filepath) as f:
		lines = f.readlines()
		split = lines[0].split(',')
		positions = [int(s) for s in split]

	minimum = min(positions)
	maximum = max(positions)
	min_fuel = 9999999999
	min_position = -1
	for i in range(minimum, maximum):
		fuel = find_fuel(positions, i)
		if fuel < min_fuel:
			min_fuel = fuel
			min_position = i

	print(min_fuel)
	print(min_position)

def find_fuel(positions, val):
	total_fuel = 0
	for p in positions:
		total_fuel += calc_rate(p, val)
		# total_fuel += abs(val - p)
	return total_fuel

def calc_rate(left, right):
	n = abs(left - right)
	fuel = (n*(n+1))//2
	return fuel

if __name__ == "__main__":
	main()