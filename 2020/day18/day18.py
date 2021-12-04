def main():
	filepath = "input.txt"
 
	sum = 0
	#with open(filepath) as fp:
	#for count, line in enumerate(fp):
	#       sum += evaluate(line)
 
	num = evaluate('1 + (2 * 3) + (4 * (5 + 6))')
	print(sum)
 
def evaluate(line):
	if(len(line) == 0):
		return 0
	if('(' not in line and ')' not in line):
		return calculateNoParen(line)
	else:
		first, last = findParens(line)
		sub = line[first+1:last]
		subEval = evaluate(sub)
		concat = line[:first-1] + str(subEval) + line[last+1:]
		return evaluate(concat)
		
def calculateNoParen(line):
	arr = line.split(' ')
	acc = int(arr[0])
	
	idx = 1
	while idx+1 < len(arr):
		ele = arr[idx+1]
		if arr[idx] == '*':
			acc *= int(ele)
		elif arr[idx] == '+':
			acc += int(ele)
		else:
			print(f'herp derp {arr[idx]}')
 
		idx += 2
	return acc
 
 
def findParens(line):
	first = line.find('(')
	open = 0
	close = 0
 
	letters = [char for char in line.strip()] 
 
	for i in range(len(letters)):
		if letters[i] == '(':
			open += 1
		elif letters[i] == ')':
			close += 1
			if open == close:
				return first, i
		
	return -1, -1
 
if __name__ == "__main__":
	main()

