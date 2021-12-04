def split(word):
    return [char for char in word]

def convert_to_dec(n_arr):
	s = "".join(n_arr)
	return int(s, 2)
	

def main():
	filepath = "input.txt"

	with open(filepath) as f:
		lines = f.readlines()

	o2 = []
	co2 = []

	for l in lines:
		o2.append(split(l.strip()))
		co2.append(split(l.strip()))
	
	#find o2 (most common)
	o2_pos = 0
	while(len(o2) > 1):
		zero_counts = count_zeros(o2)
		one_counts = count_ones(o2)

		if zero_counts[o2_pos] > one_counts[o2_pos]:
			value = 0
		else:
			value = 1
		o2 = filter_out_list(o2, o2_pos, value)
		o2_pos += 1

	#find co2 (least common)
	co2_pos = 0
	while(len(co2) > 1):
		zero_counts = count_zeros(co2)
		one_counts = count_ones(co2)

		if zero_counts[co2_pos] <= one_counts[co2_pos]:
			value = 0
		else:
			value = 1
		co2 = filter_out_list(co2, co2_pos, value)
		co2_pos += 1

	print('oxygen')
	print(convert_to_dec(o2[0]))

	print('co2')
	print(convert_to_dec(co2[0]))
	print(convert_to_dec(o2[0]) * convert_to_dec(co2[0]))


def count_zeros(lines):
	zero_counts = [0]*len(lines[0])
	size_ln = len(lines[0]) - 1
	for line in lines:
		for char_idx in range(size_ln):
			c = line[char_idx]
			if c == '0':
				zero_counts[char_idx] += 1
	return zero_counts

def count_ones(lines):
	one_counts = [0]*len(lines[0])
	size_ln = len(lines[0]) - 1
	for line in lines:
		for char_idx in range(size_ln):
			c = line[char_idx]
			if c == '1':
				one_counts[char_idx] += 1
	return one_counts

def filter_out_list(lst, position, value): 
	res = []
	for num in lst:
		if num[position] == str(value):
			res.append(num)
	return res

if __name__ == "__main__":
	main()
