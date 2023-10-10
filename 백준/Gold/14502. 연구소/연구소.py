import sys
from collections import deque
import copy

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
answer = 0

def bfs():
    safe_zone = 0
    queue = deque(virus)
    visited = copy.deepcopy(board)
    global answer

    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if not (0 <= ny < n and 0 <= nx < m):
                continue
            elif visited[ny][nx] == 0:
                visited[ny][nx] = 2
                queue.append((ny, nx))

    for i in range(n):
        safe_zone += visited[i].count(0)
    answer = max(answer, safe_zone)

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                make_wall(cnt+1)
                board[i][j] = 0

def solution():
    make_wall(0)
    print(answer)

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

virus = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus.append((i, j))
solution()
