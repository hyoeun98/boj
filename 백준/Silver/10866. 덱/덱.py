import sys
from collections import deque

n = int(sys.stdin.readline().strip())
deque = deque()
instruction = []
for _ in range(n):
    instruction.append(sys.stdin.readline().split())

for i in instruction:
    if i[0] == "push_front":
        deque.appendleft(i[-1])

    elif i[0] == "push_back":
        deque.append(i[-1])

    elif i[0] == "pop_front":
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif i[0] == "pop_back":
        if deque:
            print(deque.pop())
        else:
            print(-1)

    elif i[0] == "size":
        print(len(deque))

    elif i[0] == "empty":
        if deque:
            print(0)
        else:
            print(1)

    elif i[0] == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)

    elif i[0] == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)