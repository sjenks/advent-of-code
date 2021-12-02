def main():
	filepath = "input.txt"

	with open(filepath) as f:
		lines = f.readlines()

	horz = 0
	depth = 0
	aim = 0
	for ln in lines:
		spt = ln.split(" ")
		direction = spt[0]
		dist = int(spt[1])

		if direction == "forward":
			horz += dist
			depth += (aim * dist)
		elif direction == "down":
			aim += dist
		elif direction == "up":
			aim -= dist
		else:
			print("bad direction" + direction)
	print("horz" + str(horz))
	print("depth" + str(depth))
	print(str(horz * depth))
		

if __name__ == "__main__":
	main()
