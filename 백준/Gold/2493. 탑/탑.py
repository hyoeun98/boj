import sys
from collections import deque

n = int(sys.stdin.readline())
towers = deque(map(int, sys.stdin.readline().split()))
first = towers.popleft()
stack = [(first, 1)]
answer = [0]

for i, v in enumerate(towers):
    while stack and v > stack[-1][0]:
        del stack[-1]

    if not stack:
        answer.append(0)
    else:
        answer.append(stack[-1][1])

    stack.append((v, i+2))
for i in answer:
    print(i, end=" ")