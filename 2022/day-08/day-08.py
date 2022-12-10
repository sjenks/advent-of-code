import os
from pprint import pprint

def main_pt1():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(script_dir, "input.txt")
    with open(filepath) as f:
        lines = f.readlines()

    arr = []
    visible_arr = []
    for line in lines:
        row = []
        visible_row = []
        for char in line.strip():
            row.append(int(char))
            visible_row.append(False)
        arr.append(row)
        visible_arr.append(visible_row)
    
    #check from left to right
    for y in range(len(arr)):
        line = arr[y]
        highest_tree_seen = -1
        for x in range(len(line)):
            if arr[y][x] > highest_tree_seen:
                visible_arr[y][x] = True
                highest_tree_seen = arr[y][x]


    #check from right to left
    for y in range(len(arr)):
        line = arr[y]
        highest_tree_seen = -1
        for x in range(len(line) - 1, 0, -1):
            if arr[y][x] > highest_tree_seen:
                visible_arr[y][x] = True
                highest_tree_seen = arr[y][x]

    #check from bottom up
    for x in range(len(arr[0])):
        highest_tree_seen = -1
        for y in range(len(arr) - 1, 0, -1):
            if arr[y][x] > highest_tree_seen:
                visible_arr[y][x] = True
                highest_tree_seen = arr[y][x]

    #check from top down
    for x in range(len(arr[0])):
        highest_tree_seen = -1
        for y in range(len(arr)):
            if arr[y][x] > highest_tree_seen:
                visible_arr[y][x] = True
                highest_tree_seen = arr[y][x]

    visible_ct = 0
    for y in range(len(visible_arr)):
        line = visible_arr[y]
        for x in range(len(line)):
            if visible_arr[y][x]:
                visible_ct += 1
    print(visible_ct)

def main_pt2():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(script_dir, "input.txt")
    with open(filepath) as f:
        lines = f.readlines()

    arr = []
    for line in lines:
        row = []
        score_row = []
        for char in line.strip():
            row.append(int(char))
            score_row.append(0)
        arr.append(row)

    highest_scenic_score = 0
    find_scenic_score(arr, 2, 1)
    find_scenic_score(arr, 2, 3)
    for y in range(len(arr)):
        line = arr[y]
        for x in range(len(line)):
            score = find_scenic_score(arr, x, y)
            print(score)
            if highest_scenic_score < score:
                highest_scenic_score = score
    print('pt 2: ' + str(highest_scenic_score))

def find_scenic_score(arr, init_x, init_y):
    #check from point heading to right
    tree_height = arr[init_y][init_x]

    right_view_distance = 1
    for x in range(init_x + 1, len(arr[0]) - 1):
        if arr[init_y][x] >= tree_height:
            break
        else:
            right_view_distance += 1


    #check from point heading left
    left_view_distance = 1
    for x in range(init_x - 1, 0, -1):
        if arr[init_y][x] >= tree_height:
            break
        else:
            left_view_distance += 1


    #check from point heading up
    up_view_distance = 1
    for y in range(init_y - 1, 0, -1):
        if arr[y][init_x] >= tree_height:
            break
        else:
            up_view_distance += 1

    #check from point heading down
    down_view_distance = 1
    for y in range(init_y + 1, len(arr)-1):
        if arr[y][init_x] >= tree_height:
            break
        else:
            down_view_distance += 1
            

    return down_view_distance * up_view_distance * left_view_distance * right_view_distance

if __name__ == "__main__":
    main_pt1()
    main_pt2()