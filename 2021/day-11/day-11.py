import os
def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(script_dir, "input.txt")
    with open(filepath) as f:
        lines = f.readlines()
    
    grid = []
    for line in lines:
        grid.append([int(l) for l in line.strip()])
    print(grid)
    flash_sum = 0
    for i in range(500):
        print(i)
        print('-----------------')
        print(grid)
        grid, flashes = next_iteration(grid)
        if flashes ==  100:
            print('all flashing!')
            print(i)
            break
        flash_sum += flashes

    print('---')
    print(flash_sum)


def next_iteration(grid):
    next = []
    for line in grid:
        next.append([0] * len(grid[0]))

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            next[y][x] = grid[y][x] + 1
    
    next, flashes = check_flash(next)
    return next, flashes
    
def check_flash(grid):
    flash_list = []

    while True:
        flashed = False
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] > 9 and (x,y) not in flash_list:
                    #flash
                    flashed = True
                    flash_list.append((x,y))
                    adj_cells = get_adjacent(grid, x, y)
                    #increment adjacent for "flash"
                    for adj in adj_cells:
                        grid[adj[1]][adj[0]] = grid[adj[1]][adj[0]] + 1
        if not flashed:
            for f in flash_list:
                grid[f[1]][f[0]] = 0

            return grid, len(flash_list)
                    
def get_adjacent(grid, x, y):
    adjacent = []
    adjacent.append((x - 1, y - 1))
    adjacent.append((x - 1, y))
    adjacent.append((x - 1, y + 1))

    adjacent.append((x, y - 1))
    adjacent.append((x, y + 1))
    
    adjacent.append((x + 1, y - 1))
    adjacent.append((x + 1, y))
    adjacent.append((x + 1, y + 1))
    
    filtered = []
    for a in adjacent:
        if a[0] >= 0 and a[0] < len(grid):
            if a[1] >= 0 and a[1] < len(grid[0]):
                filtered.append(a)
    return filtered
    
if __name__ == "__main__":
    main()