import sys
from collections import deque
from pprint import pprint

def bfs(board, tomato_q, visited):
    dz = [0, 0, 0, 0, 1, -1]
    dy = [0, 0, 1, -1, 0, 0]
    dx = [1, -1, 0, 0, 0 ,0]

    while tomato_q:
        z, y, x = tomato_q.popleft()
        for idx in range(6):
            nz, ny, nx = z + dz[idx], y + dy[idx], x + dx[idx]
            if not (0 <= nz < h and 0 <= ny < n and 0 <= nx < m):
                continue
            if board[nz][ny][nx] == 0 and visited[nz][ny][nx] == 0:
                visited[nz][ny][nx] = visited[z][y][x] + 1
                tomato_q.append((nz, ny, nx))

def solution():
    board = []
    visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
    for _ in range(h):
        temp = []
        for _ in range(n):
            temp.append(list(map(int, sys.stdin.readline().split())))
        board.append(temp)
    
    tomato_q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 1:
                    # bfs(board, i, j, k, visited)
                    tomato_q.append((i, j, k))
                    visited[i][j][k] = 1
                elif board[i][j][k] == -1:
                    visited[i][j][k] = -1

    bfs(board, tomato_q, visited)
    answer = 0
    # pprint(visited)
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if visited[i][j][k] == 0:
                    print(-1)
                    return
                elif visited[i][j][k] != -1:
                    answer = max(answer, visited[i][j][k])
    
    print(answer - 1)


m, n, h = map(int, sys.stdin.readline().split())
solution()