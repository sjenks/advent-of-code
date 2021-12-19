import os
def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(script_dir, "input.txt")
    with open(filepath) as f:
        lines = f.readlines()

    points = 0
    for line in lines:
        error = find_error(line.strip())
        pts = find_points(error)
        print(line.strip() + "     " + str(error) + "    " + str(pts))
        points += pts
    print(str(points))

# def find_corrupt(line):
#     points = {}
#     points[''] = 0
#     points['('] = 0
#     points['['] = 0
#     points['{'] = 0
#     points['<'] = 0
#     opening_paren = '([{<'

#     for char in line:
#         if char in opening_paren:
#             points[char] = points[char] + 1
#         else:
#             if points[char
#             points[char] = points[char] - 1

def find_error(line):
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
                    print(f' expected {expected_close} but found {char} ')
                    return char
                    
    return ''

def find_points(char):
    points = {}
    points[''] = 0
    points[')'] = 3
    points[']'] = 57
    points['}'] = 1197
    points['>'] = 25137
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