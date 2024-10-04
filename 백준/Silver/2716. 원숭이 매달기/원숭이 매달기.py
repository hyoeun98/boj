import sys
import re
from collections import deque

n = int(sys.stdin.readline())
for _ in range(n):
    case = sys.stdin.readline().strip()
    if not case:
        print(1)
    else:
        cnt = 0
        while case:
            case = case.replace("[]", "")
            cnt += 1
        print(2 ** cnt) 