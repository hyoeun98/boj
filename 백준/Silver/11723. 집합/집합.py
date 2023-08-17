import sys
import copy 
def solution():
    m = int(sys.stdin.readline())
    S = set()
    all_set = set(range(1, 21))
    for _ in range(m):
        temp = sys.stdin.readline().split()
        if len(temp) == 1:
            operator, operand = temp[0], 0
        else:
            operator, operand = temp[0], int(temp[1])

        if operator == "add":
            S.add(operand)
        elif operator == "remove" and operand in S:
            S.remove(operand)
        elif operator == "check":
            if operand in S:
                print(1)
            else:
                print(0)
        elif operator == "toggle":
            if operand in S:
                S.remove(operand)
            else:
                S.add(operand)
        elif operator == "all":
            S = set(range(1, 21))
        elif operator == "empty":
            S.clear()

solution()
