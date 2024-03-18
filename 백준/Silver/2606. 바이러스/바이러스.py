import sys
from collections import deque
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
answer = set()
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    board[a][b] = 1
    board[b][a] = 1
    
candidate = deque([i for i, v in enumerate(board[1]) if v == 1])
while candidate:
    next = candidate.popleft()
    answer.add(next)
    candidate.extend([i for i, v in enumerate(board[next]) if v == 1 and i not in answer])
    
print(len(answer) - 1 if answer else 0)