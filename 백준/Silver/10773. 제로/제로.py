import sys
from collections import deque

k = int(sys.stdin.readline())
stack = deque()
for _ in range(k):
    temp = int(sys.stdin.readline())
    if temp == 0:
        stack.pop()
    else:
        stack.append(temp)

print(sum(stack))