import sys
from collections import deque
from pprint import pprint
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(board):
    queue = deque()
    queue.append((0, 0, 0, 0)) # y, x, flag, cnt

    visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    
    while queue:
        y, x, flag, cnt = queue.popleft()
        # print(y, x, flag, cnt)
        if y == (n - 1) and x == (m - 1):
            print(cnt + 1)
            return
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if not(0 <= ny < n and 0 <= nx < m):
                continue
            if visited[ny][nx][flag] == 1:
                continue

            if flag == 0: # 벽 부수기 전
                queue.append((ny, nx, int(board[ny][nx]), cnt + 1))
                visited[ny][nx][int(board[ny][nx])] = 1
            elif flag == 1 and board[ny][nx] == "0":
                queue.append((ny, nx, 1, cnt + 1))
                visited[ny][nx][flag] = 1
    
    print(-1)

def solution():
    board = []
    for _ in range(n):
        board.append(list(sys.stdin.readline().strip()))
    
    bfs(board)
n, m = map(int, sys.stdin.readline().split())
solution()