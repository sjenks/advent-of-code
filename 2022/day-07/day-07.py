import os
from typing import List, Set, Dict, Tuple

class INode:
    def __init__(self, size: int, name: str, contents: List[any], parent: any):
        self.size = size
        self.name = name
        self.contents = contents
        self.parent = parent

    def add(self, child):
        self.size += child.size
        self.contents.append(child)
    

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(script_dir, "input.txt")
    with open(filepath) as f:
        lines = f.readlines()

    stack = []
    directory_tree = INode(0, '/', [], None)

    while i < len(lines):
        line = lines[i]
        if line.startswith('$'):
            argv = line.split(' ')
            if argv[1] == 'ls':
                current_command = True
            elif argv[1] == 'cd':
                current_command_ls = False
        else: #ls command results
            
        i += 1            
if __name__ == "__main__":
    main()