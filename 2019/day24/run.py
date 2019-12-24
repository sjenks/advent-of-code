
def main():
	grid = parse()
	for i in range(4):
		print("after min", i)
		printGrid(grid)		
		nextState = [x[:] for x in [['.'] * 5] * 5] 
		for y in range(5):
			for x in range(5):
				if spotInfested((x,y), grid):
					nextState[y][x] = '#'
		grid = nextState


def parse():
	filename = "test.txt"
	#list(string) casts into array of chars
	lines = [list(line) for line in open(filename).read().split("\n")[:-1]]
	return lines

def spotInfested(p, grid):
	numBugs = 0
	left = (p[0] - 1, p[1])
	if(hasBug(left, grid)):
		numBugs += 1

	right = (p[0] + 1, p[1])
	if(hasBug(right, grid)):
		numBugs += 1
		
	up = (p[0], p[1] - 1)
	if(hasBug(up, grid)):
		numBugs += 1

	down = (p[0], p[1] + 1)
	if(hasBug(down, grid)):
		numBugs += 1
	
	curBug = hasBug(p, grid)
	if curBug:
		if numBugs != 1:
			return False
		else:
			return True
	else:
		if numBugs == 1 or numBugs == 2:
			return True
		else:
			return False

def printGrid(grid):
	for y in range(len(grid)):
		s = ""
		for x in range(len(grid[y])):
			s = s + grid[y][x]
		print(s)

def hasBug(position, grid):
	if position[1] < 0 or position[1] >= len(grid):
		return False
	if position[0] < 0 or position[0] >= len(grid[0]):
		return False
	return grid[position[1]][position[0]] == '#'

if __name__ == "__main__":
	main()