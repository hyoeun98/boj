import sys
from collections import deque
from pprint import pprint

def fire_bfs(board, fire_q, f_visited):
    dy = [0, 0, 1, -1]
    dx = [1, -1 ,0 ,0]

    while fire_q:
        y, x = fire_q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < r and 0 <= nx < c and board[ny][nx] != "#" and f_visited[ny][nx] == 0:
                fire_q.append((ny, nx))
                f_visited[ny][nx] = f_visited[y][x] + 1

def jihoon_bfs(board, jihoon_q, j_visited, f_visited):
    dy = [0, 0, 1, -1]
    dx = [1, -1 ,0 ,0]

    while jihoon_q:
        y, x = jihoon_q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            
            if 0 <= ny < r and 0 <= nx < c:
                if board[ny][nx] != "#" and j_visited[ny][nx] == 0:
                    if f_visited[ny][nx] == 0 or f_visited[ny][nx] > j_visited[y][x] + 1:
                        j_visited[ny][nx] = j_visited[y][x] + 1
                        jihoon_q.append((ny, nx))

            else:
                print(j_visited[y][x])
                return
    
    print("IMPOSSIBLE")
    

def solution():
    board = []
    for _ in range(r):
        board.append(list(sys.stdin.readline().strip()))
    f_visited = [[0 for _ in range(c)] for _ in range(r)]
    j_visited = [[0 for _ in range(c)] for _ in range(r)]

    fire_q = deque()
    for i in range(r):
        for j in range(c):
            if board[i][j] == "F":
                f_visited[i][j] = 1
                fire_q.append((i, j))

    fire_bfs(board, fire_q, f_visited)

    jihoon_q = deque()
    for i in range(r):
        for j in range(c):
            if board[i][j] == "J":
                j_visited[i][j] = 1
                jihoon_q.append((i, j))

    jihoon_bfs(board, jihoon_q, j_visited, f_visited)

    # print(f_visited)
    # print(j_visited)

r, c = map(int,sys.stdin.readline().split())
solution()


