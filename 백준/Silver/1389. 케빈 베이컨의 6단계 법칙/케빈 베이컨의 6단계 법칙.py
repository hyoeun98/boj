import sys    
from collections import deque

def bfs(start):
    queue = deque()
    queue.append((start, 1))
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    elapsed_time = 0
    while queue:
        node, distance = queue.popleft()
        next_node = [i for i, v in enumerate(board[node]) if v == 1]
        for i in next_node:
            if not visited[i]:
                elapsed_time += distance
                visited[i] = True
                queue.append((i, distance + 1))
    
    return elapsed_time
n, m = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    board[a][b] = 1
    board[b][a] = 1
    
kevin_bacon = 1e9
for i in range(1, n + 1):
    temp = bfs(i)
    if temp < kevin_bacon:
        answer = i
        kevin_bacon = temp

print(answer)