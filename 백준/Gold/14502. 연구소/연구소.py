import sys
from collections import deque
import itertools as it
import copy

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(board, virus, wall):
    
    safe_zone = 0
    queue = deque(virus)
    visited = copy.deepcopy(board)
    for i, j in wall:
        visited[i][j] = 1
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

    return safe_zone
    
def solution():
    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))
    
    space = []
    virus = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                space.append((i, j))
            elif board[i][j] == 2:
                virus.append((i, j))
    
    walls = list(it.combinations(space, 3))
    answer = 0
    for wall in walls:
        answer = max(answer, bfs(board, virus, wall))

    print(answer)
n, m = map(int, sys.stdin.readline().split())

solution()
