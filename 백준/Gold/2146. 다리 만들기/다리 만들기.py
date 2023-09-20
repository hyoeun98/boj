import sys
from collections import deque
from pprint import pprint

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def divide_island(i, j, board, cnt):
    queue = deque()
    queue.append((i, j))
    board[i][j] = cnt
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if board[ny][nx] == 1:
                board[ny][nx] = cnt
                queue.append((ny, nx))

def make_bridge(i, board):
    queue = deque()
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            if board[a][b] == i:
                queue.append((a, b))
                distance[a][b] = 0

    while queue:
        y, x = queue.popleft()
        # print(y, x)
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if board[ny][nx] > 0 and board[ny][nx] != i:

                return distance[y][x]
            elif board[ny][nx] == 0 and distance[ny][nx] == -1:
                distance[ny][nx] = distance[y][x] + 1
                queue.append((ny, nx))
def solution():
    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))

    cnt = 2
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                divide_island(i, j, board, cnt)
                cnt += 1
    
    answer = 1000
    for i in range(2, cnt):
        answer = min(answer, make_bridge(i, board))
    print(answer)

n = int(sys.stdin.readline())
solution()