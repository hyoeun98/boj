import sys
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in board[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                
n, m = map(int, sys.stdin.readline().split())
board = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
answer = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    board[a].append(b)
    board[b].append(a)

for i in range(1, n + 1):
    if not visited[i]:
        if not board[i]:
            answer += 1
            visited[i] = True
        else:
            bfs(i)
            answer += 1
            
print(answer)

    
    

