import sys
from collections import deque

n = int(sys.stdin.readline())
board = [[] for i in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    board[a].append(b)
    board[b].append(a)

queue = deque()
queue.append(1)
answer = [0 for _ in range(n + 1)]

while queue:
    current = queue.popleft()
    for sub in board[current]:
        if answer[sub] == 0:
            answer[sub] = current
            queue.append(sub)

for i in answer[2:]:
    print(i)
