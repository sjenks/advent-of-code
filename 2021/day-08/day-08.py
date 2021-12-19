import os
def main():
	script_dir = os.path.dirname(os.path.realpath(__file__))
	filepath = os.path.join(script_dir, "input.txt")
	with open(filepath) as f:
		lines = f.readlines()

		total = 0
		for line in lines:
			io_line = line.strip().split('|')
			output_str = io_line[1]
			pattern_str = io_line[0]
			unsorted_patt_ln = (pattern_str.strip().split(' '))
			unsorted_output_ln = (output_str.strip().split(' '))

			patt_ln = [sorted(n) for n in unsorted_patt_ln]
			output_ln = [sorted(n) for n in unsorted_output_ln]

			nums_arr = find_nums_arr(patt_ln)

			output_translated = ""
			for out in output_ln:
				digit = nums_arr.index(out)
				output_translated = output_translated + str(digit)
			total += int(output_translated)
		print(total)

	# pt 1
	# counts = [0]*10
	# for ln in output:
	# 	for n in ln:
	# 		if len(n) == 2:
	# 			counts[1] = counts[1] + 1
	# 		elif len(n) == 4:
	# 			counts[4] = counts[4] + 1
	# 		elif len(n) == 3:
	# 			counts[7] = counts[7] + 1
	# 		elif len(n) == 7:
	# 			counts[8] = counts[8] + 1
	# print(counts)
	# print(str(sum(counts)))

def find_nums_arr(ln):
	nums = []
	nums.append(find_zero(ln))
	nums.append(find_one(ln))
	nums.append(find_two(ln))
	nums.append(find_three(ln))
	nums.append(find_four(ln))
	nums.append(find_five(ln))
	nums.append(find_six(ln))
	nums.append(find_seven(ln))
	nums.append(find_eight(ln))
	nums.append(find_nine(ln))
	return nums

def find_six(ln):
	one = find_one(ln)
	for n in ln:
		if (len(n) == 6) and any(c not in n for c in one):
			return n

def find_zero(ln):
	four = find_four(ln)
	six = find_six(ln)
	for n in ln:
		if (len(n) == 6) and any(c not in n for c in four) and (n != six):
			return n

def find_nine(ln):
	zero = find_zero(ln)
	six = find_six(ln)
	for n in ln:
		if len(n) == 6 and (n != zero) and (n != six):
			return n

def find_five(ln):
	six = find_six(ln)
	for n in ln:
		if len(n) == 5 and all(c in six for c in n):
			return n

def find_three(ln):
	nine = find_nine(ln)
	five = find_five(ln)
	for n in ln:
		if len(n) == 5 and all(c in nine for c in n) and n != five:
			return n

def find_two(ln):
	five = find_five(ln)
	three = find_three(ln)
	for n in ln:
		if len(n) == 5 and (n != five) and (n != three):
			return n

def find_one(ln):
	for n in ln:
		if len(n) == 2:
			return n

def find_four(ln):
	for n in ln:
		if len(n) == 4:
			return n

def find_seven(ln):
	for n in ln:
		if len(n) == 3:
			return n

def find_eight(ln):
	for n in ln:
		if len(n) == 7:
			return n
if __name__ == "__main__":
	main()