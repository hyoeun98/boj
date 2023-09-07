import sys
from collections import deque
def bfs(board, i, j):
    dy = [1, -1, 0 ,0]
    dx = [0, 0, 1, -1]
    queue = deque()
    queue.append([i, j])
    board[i][j] = 0
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if not (0 <= ny < n and 0 <= nx < m):
                continue
            if board[ny][nx] == 1:
                cnt += 1
                board[ny][nx] = 0
                queue.append([ny, nx])
                
    return cnt

def solution():
    board = []
    num_paint = 0
    max_paint = 0
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                max_paint = max(max_paint, (bfs(board, i, j)))
                num_paint += 1
    print(num_paint)
    print(max_paint)
n , m = map(int, sys.stdin.readline().split())
solution()
