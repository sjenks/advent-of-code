import os
def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(script_dir, "input.txt")
    with open(filepath) as f:
        instructions = f.readlines()
    stacks = input_stack()
    
    for line in instructions:
        splt = line.split(' from ')
        move = splt[1].split(' to ')
        stacks = perform_stack_move(int(splt[0]), int(move[0]), int(move[1]), stacks)
    
        print(stacks)
        print('----')

    for cur in stacks:
        print(cur[0], end='')
    print()


def perform_move(num_boxes, source, dest, stacks):
    for i in range(num_boxes):
        box = stacks[source - 1].pop(0)
        stacks[dest - 1].insert(0, box)
    return stacks

def perform_stack_move(num_boxes, source, dest, stacks):
    boxes = [] # DNZ
    for i in range(num_boxes):
        boxes.append(stacks[source - 1].pop(0))

    boxes.reverse()
    for b in boxes:
        stacks[dest - 1].insert(0, b)
    return stacks

def small_stack():
    res = []
    res.append(['N', 'Z'])
    res.append(['D', 'C', 'M'])
    res.append(['P'])
    return res

def input_stack():
    res = []
    res.append(['V', 'Q', 'W', 'M', 'B', 'N', 'Z', 'C'])
    res.append(['B', 'C', 'W', 'R', 'Z', 'H'])
    res.append(['J', 'R', 'Q', 'F'])
    res.append(['T', 'M', 'N', 'F', 'H', 'W', 'S', 'Z' ])
    res.append(['P', 'Q', 'N', 'L', 'W', 'F', 'G'])
    res.append(['W', 'P', 'L'])
    res.append(['J', 'Q', 'C', 'G', 'R', 'D', 'B', 'V' ])
    res.append(['W', 'B', 'N', 'Q', 'Z'])
    res.append(['J', 'T', 'G', 'C', 'F', 'L', 'H' ])
    return res	

if __name__ == "__main__":
    main()