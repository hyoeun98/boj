import sys
from collections import deque

def bfs(board, i, j):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    queue = deque()
    queue.append((i, j))
    board[i][j] = 0
    area = 1
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 1:
                area += 1
                queue.append((ny, nx))
                board[ny][nx] = 0
    return area

def solution():
    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().strip())))

    num_apt = 0
    areas = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                num_apt += 1
                areas.append(bfs(board, i, j))    
    

    print(num_apt)
    areas.sort()
    for i in areas:
        print(i)


n = int(sys.stdin.readline())
solution()


