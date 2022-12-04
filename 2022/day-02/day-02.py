import os
def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(script_dir, "input.txt")
    with open(filepath) as f:
        lines = f.readlines()
    
    total_score = 0
    for line in lines:
        chars = line.strip().split(' ')
        second_char = find_second_char(chars[0], chars[1])
        score = win_score(chars[0], second_char) + char_to_score(second_char)
        print(score)
        total_score += score

    print(total_score)

def find_second_char(elf, outcome):
    

    if outcome == 'X': # lose
        if elf == 'A':
            return 'Z'
        if elf == 'B':
            return 'X'
        if elf == 'C':
            return 'Y'
    if outcome == 'Y': # draw
        x_offset = ord('X') - ord('A')
        return chr(ord(elf) + x_offset)
    if outcome == 'Z': # win
        if elf == 'A':
            return 'Y'
        if elf == 'B':
            return 'Z'
        if elf == 'C':
            return 'X'

def win_score(elf, self):
    # need to shift x to a to compare for equality
    if ord(elf) - ord('A') == ord(self) - ord('X'):
        return 3
    # self wins
    if elf == 'A' and self == 'Y':
        return 6
    if elf == 'B' and self == 'Z':
        return 6
    if elf == 'C' and self == 'X':
        return 6
    # not tie, self didn't win, elf won
    return 0


def char_to_score(char):
    if char == 'X': # A rock
        return 1
    elif char == 'Y': # B paper
        return 2
    elif char == 'Z': # C scissors
        return 3
    print('unknown score' + char)

if __name__ == "__main__":
    main()