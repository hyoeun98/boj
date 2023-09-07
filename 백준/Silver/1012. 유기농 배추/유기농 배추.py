import sys
from collections import deque
def bfs(board, i, j):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    queue = deque()
    queue.append((i, j))
    board[i][j] = 0
    
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 1:
                board[ny][nx] = 0
                queue.append((ny, nx))

def solution(board):
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                bfs(board, i, j)
                answer += 1
    print(answer)
T = int(sys.stdin.readline())
for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    board = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        board[y][x] = 1
    
    solution(board)


