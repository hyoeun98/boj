import sys
from collections import deque

bracket_dict = dict()
bracket_dict["("] = ")"
bracket_dict["["] = "]"

while True:
    seq = sys.stdin.readline().rstrip()
    if seq == ".":
        break
    
    valid_flag = True
    stack = deque()

    for i in seq:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")" or i == "]":
            if stack and bracket_dict[stack.pop()] == i:
                pass
            else:
                valid_flag = False
                break
    if stack:
        valid_flag = False
    print("yes" if valid_flag else "no")
    
