from collections import deque

from more_itertools import adjacent

def main():
	filepath = "input.txt"
	grid = []
	with open(filepath) as f:
		lines = f.readlines()
		for y in lines:
			grid.append([int(c) for c in y.strip()])
	
	risk_level = 0
	lowest_levels = []
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if is_lower_adj(grid, x, y):
				# print(f'adding {grid[y][x]}')
				risk_level += (grid[y][x] + 1)
				lowest_levels.append(grid[y][x])
	print("risk level")
	print(risk_level)

	sizes = []
	visited = []
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] < 9 and (x,y) not in visited:
				sizes.append(flood_fill_size(grid, visited, x, y))
	print("basin sizes")
	sizes.sort()
	print(sizes)

def flood_fill_size(grid, visited, x, y):
	queue = deque()
	queue.append((x,y))
	size = 0
	visited.append((x,y))
	while(len(queue) > 0):
		ele = queue.popleft()
		size += 1
		adjacent = get_adjacent_positions(grid, ele[0], ele[1])
		for a in adjacent:
			value = grid[a[1]][a[0]]
			if value < 9 and a not in visited:
				queue.append(a)
				visited.append(a)
	return size

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

def get_adjacent_positions(grid, x, y):
	adj = []
	if y-1 >= 0:
		adj.append((x,y-1))
	if y+1 < len(grid):
		adj.append((x,y+1))
	if x+1 < len(grid[y]):
		adj.append((x+1,y))
	if x-1 >= 0:
		adj.append((x-1,y))
	return adj

if __name__ == "__main__":
	main()
