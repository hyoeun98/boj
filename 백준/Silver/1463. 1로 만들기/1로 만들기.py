import sys
from collections import deque
def solution():
    queue = deque()
    queue.append((n, 0))

    while queue:
        temp, cnt = queue.popleft()
        if temp == 1:
            print(cnt)
            break
        if temp % 3 == 0:
            queue.append((temp // 3, cnt + 1))
        if temp % 2 == 0:
            queue.append((temp // 2, cnt + 1))
        queue.append((temp - 1, cnt + 1))

n = int(sys.stdin.readline())
solution()