import os
def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(script_dir, "input.txt")
    with open(filepath) as f:
        lines = f.readlines()

    points = 0
    all_points = []
    for line in lines:
        error = find_corrupt(line.strip())
        pts = find_points(error)
        #print(line.strip() + "     " + str(error) + "    " + str(pts))
        points += pts
        all_points.append(points)
    print(f'total points{points}')
    all_points.sort()
    half_idx = len(all_points) // 2
    print(f'middle {all_points[half_idx]}')

def find_corrupt(line):
    opening_paren = '([{<'
    close_paren = ')]}>'

    stack = []
    for char in line:
        if char in opening_paren:
            stack.append(char)
        else:
            if len(stack) == 0:
                #ignore incomplete lines?
                return ''
            else: 
                opening = stack.pop()
                expected_close = flip(opening)
                if expected_close != char:
                    #print(f' expected {expected_close} but found {char} ')
                    return char
                    
    return ''

def find_points(char):
    points = {'' : 0, ')': 3, ']': 57, '}': 1197, '>': 25137}

    return points[char]

def flip(char):
    points = {}
    points['('] = ')'
    points['['] = ']'
    points['{'] = '}'
    points['<'] = '>'
    return points[char]

def flop_open(char):
    points = {}
    points[')'] = '('
    points[']'] = '['
    points['}'] = '{'
    points['>'] = '<'
    return points[char]
                
def idx(char, string):
    idx = 0
    for s in string:
        if char == s:
            return idx
        idx += 1
    return -1

if __name__ == "__main__":
    main()