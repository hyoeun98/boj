import sys
from collections import deque    
def bfs(board, visited, i, j, s):
    dy = [0, 0, 1, -1]
    dx = [1, -1 ,0, 0]

    visited.add((i, j))
    queue = deque()
    queue.append((i, j))
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if (ny, nx) not in visited and 0 <= ny < n and 0 <= nx < n and board[ny][nx] > s:
                visited.add((ny, nx))
                queue.append((ny, nx))
def solution():
    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))

    max_area = 0
    for s in range(101):
        visited = set()
        current_area = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] > s and (i, j) not in visited:
                    bfs(board, visited, i, j, s)
                    current_area += 1
        max_area = max(max_area, current_area)
    print(max_area)
n = int(sys.stdin.readline())
solution()


