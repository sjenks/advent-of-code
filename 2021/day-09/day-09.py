def main():
	filepath = "input.txt"
	grid = []
	with open(filepath) as f:
		lines = f.readlines()
		for y in lines:
			grid.append([int(c) for c in y.strip()])
	
	risk_level = 0
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if is_lower_adj(grid, x, y):
				print(f'adding {grid[y][x]}')
				risk_level += (grid[y][x] + 1)
	print(risk_level)

def is_lower_adj(grid, x, y):
	adj = get_adjacent(grid, x, y)
	curr = grid[y][x]
	return all(c > curr for c in adj)

def get_adjacent(grid, x, y):
	adj = []
	if y-1 >= 0:
		adj.append(grid[y-1][x])
	if y+1 < len(grid):
		adj.append(grid[y+1][x])
	if x+1 < len(grid[y]):
		adj.append(grid[y][x+1])
	if x-1 >= 0:
		adj.append(grid[y][x-1])
	return adj

if __name__ == "__main__":
	main()