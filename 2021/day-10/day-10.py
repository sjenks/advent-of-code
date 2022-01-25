import os
def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(script_dir, "input.txt")
    with open(filepath) as f:
        lines = f.readlines()

    corrupt_points = 0
    incomplete_points = []
    for line in lines:
        error = find_corrupt(line.strip())
        pts = find_corrupt_points(error)
        corrupt_points += pts

        if pts == 0:
            incomplete_pt = find_incomplete_points(line.strip())
            incomplete_points.append(incomplete_pt)

    print(f'corrupt points {corrupt_points}')
    incomplete_points.sort()
    print(incomplete_points)
    half_idx = len(incomplete_points) // 2
    print(f'middle {incomplete_points[half_idx]}')
    
def find_incomplete_points(line):
    opening_paren = '([{<'
    
    stack = []
    for char in line:
        if char in opening_paren:
            stack.append(char)
        else:
            if len(stack) == 0:
                return ''
            else: 
                opening = stack.pop()
                expected_close = flip(opening)
                if expected_close != char:
                    break
    pts_map = {')' : 1, ']': 2, '}': 3, '>': 4}
    points = 0
    for char in reversed(stack):
        points = points * 5
        close = flip(char)
        points += pts_map[close]

    return points
    

def find_corrupt(line):
    opening_paren = '([{<'
    
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

def find_corrupt_points(char):
    points = {'' : 0, ')': 3, ']': 57, '}': 1197, '>': 25137}

    return points[char]

def flip(char):
    points = {}
    points['('] = ')'
    points['['] = ']'
    points['{'] = '}'
    points['<'] = '>'
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