import os
def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(script_dir, "input.txt")
    with open(filepath) as f:
        lines = f.readlines()

    pri_sum = 0
    elves = []
    for line in lines:
        line = line.strip()
        line_len = int(len(line)/2)
        
        first_half = line[0:line_len]
        second_half = line[line_len:len(line)]
        intersect = intersection(first_half, second_half)
        print(intersect)
        elves.append(list(intersect)[0])
        for char in intersect:
            pri_sum += priority(char)
    print(pri_sum)
    part2(lines)


def part2(lines):
    pri_sum = 0
    i = 0
    while i + 2 < len(lines):
        first_two = intersection(lines[i].strip(), lines[i+1].strip())
        overall = intersection(first_two, lines[i+2].strip())
        if len(overall) > 0:
            pri_sum += priority(list(overall)[0])
        i += 3
    print(pri_sum)



def intersection(lst1, lst2):
    intersect = [value for value in lst1 if value in lst2]
    return set(intersect)

def priority(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27

if __name__ == "__main__":
    main()