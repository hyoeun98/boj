import sys
from collections import deque

def bfs(start_y, start_x):
    answer[start_y][start_x] = 0
    visited[start_y][start_x] = True
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    queue = deque()
    queue.append((start_y, start_x))
    
    while queue:
        ny, nx = queue.popleft()
        current_distance = answer[ny][nx]
        for i in range(4):
            y, x = ny + dy[i], nx + dx[i]
            if 0 > y or y >= n or 0 > x or x >= m:
                continue
            if not visited[y][x]:
                if board[y][x] == 0:
                    answer[y][x] = 0
                else:
                    answer[y][x] = current_distance + 1
                    queue.append((y, x))
                visited[y][x] = True
            
        
    

n, m = map(int,sys.stdin.readline().split())
board = []
visited = [[False for _ in range(m)] for _ in range(n)]
answer = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    if 2 in line:
        start_y, start_x = i, line.index(2)    
    board.append(line)
    
bfs(start_y, start_x)
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            answer[i][j] = 0
for i in answer:
    print(*i)
