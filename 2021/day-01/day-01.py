def main():
	filepath = "input.txt"

	with open(filepath) as f:
		lines = f.readlines()

		sliding = []
		length = len(lines)
		for i in range(length - 2):
			tot = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
			sliding.append(tot)

		print(sliding)
		increased = -1 # will increase on #0
		last = 0
		for l in sliding:
			if l > last:
				increased += 1
			last = l
		
		print(increased)

if __name__ == "__main__":
	main()