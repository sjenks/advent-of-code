from copy import deepcopy

def main():
	state = parse()
	print(str(state))

	cycles = 6
	for i in range(cycles):

	
def nextCycle(state):
	nextState = deepcopy(state)
	for x in 

def parse():
	filepath = "input.txt"

	inputArr = []

	with open(filepath) as fp:
		for count, line in enumerate(fp):
			letters = [char for char in line.strip()]  
			inputArr.append(letters)
	return inputArr

if __name__ == "__main__":
	main()