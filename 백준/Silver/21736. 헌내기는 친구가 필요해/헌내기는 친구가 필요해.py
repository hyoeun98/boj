import sys    
from collections import deque

def bfs(start_y, start_x):
    queue = deque()
    queue.append((start_y, start_x))
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    answer = 0
    while queue:
        ny, nx = queue.popleft()
        for i in range(4):
            y, x = ny + dy[i], nx + dx[i]
            if y < 0 or y >= n or x < 0 or x >= m:
                continue
            elif visited[y][x] or board[y][x] == "X":
                continue
            else:
                if board[y][x] == "P":
                    answer += 1
                visited[y][x] = True
                queue.append((y, x))
    
    return answer
n, m = map(int, sys.stdin.readline().split())
board = []
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    row = sys.stdin.readline().strip()
    board.append(row)
    if "I" in row:
        start_y, start_x = i, row.index("I")
        
answer = bfs(start_y, start_x)
print(answer if answer > 0 else "TT")

