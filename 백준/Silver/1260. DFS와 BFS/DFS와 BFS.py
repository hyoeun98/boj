import sys    
from collections import deque

def dfs(start):
    dfs_answer.append(start)
    dfs_visited[start] = True 
    candidate = [i for i, v in enumerate(board[start]) if v == 1]
    for i in candidate:
        if not dfs_visited[i]:
            dfs(i)
    
    
def bfs(start):
    queue = deque()    
    queue.append(start)
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    answer = []
    while queue:
        current = queue.popleft()
        answer.append(current)
        for i, v in enumerate(board[current]):
            if v == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True
    
    print(*answer)
n, m, v = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    board[a][b] = 1
    board[b][a] = 1
    
dfs_answer = []
dfs_visited = [False for _ in range(n + 1)]

dfs(v)
print(*dfs_answer)
bfs(v)
