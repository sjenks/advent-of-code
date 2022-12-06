import os
def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(script_dir, "input.txt")
    with open(filepath) as f:
        line = f.readlines()

    buff = []
    idx = 0
    for char in line[0]:
        buff.append(char)
        if all_different(buff):
            print(idx + 1)
            return
        if len(buff) == 14:
            buff.pop(0)         
        idx += 1
    print('none found?')

def all_different(buff):
    if len(buff) < 14:
        return False
    buff_set = set(list(buff))
    if len(buff_set) == 14:
        return True
    return False

if __name__ == "__main__":
    main()