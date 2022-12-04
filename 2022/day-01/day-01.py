def main():
	filepath = "input.txt"

	with open(filepath) as f:
		lines = f.readlines()

	total = 0
	max_sum = 0
	all_cals = []
	for l in lines:
		if l.strip() == "":
			all_cals.append(total)
			total = 0

		else:
			cur = int(l.strip())
			#print(cur)
			total += cur
			if total > max_sum:
				max_sum = total
	
	all_cals.sort(reverse = True)
	print(sum(all_cals[0:3]))
if __name__ == "__main__":
	main()
