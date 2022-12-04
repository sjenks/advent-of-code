import os
def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(script_dir, "input.txt")
    with open(filepath) as f:
        lines = f.readlines()
    
    full_contained_ct = 0
    overlap_ct = 0
    for line in lines:
        pairs = line.strip().split(',')
        left = pairs[0].split('-')
        right = pairs[1].split('-')
        if fully_contained(int(left[0]), int(left[1]), int(right[0]), int(right[1])):
            full_contained_ct += 1
        if overlap(int(left[0]), int(left[1]), int(right[0]), int(right[1])):
            overlap_ct += 1
    
    print(full_contained_ct)
    print(overlap_ct)

def fully_contained(l_start, l_end, r_start, r_end):
    # l_start r_start r_end l_end
    if l_start <= r_start and r_end <= l_end: # l is outer
        return True
    # l_start r_start r_end l_end
    if r_start <= l_start and l_end <= r_end: # r is outer
        return True
    return False

def overlap(l_start, l_end, r_start, r_end):
    if l_start >= r_start and l_start <= r_end: 
        return True
    if r_start >= l_start and r_start <= l_end:
        return True
    return False

if __name__ == "__main__":
    main()