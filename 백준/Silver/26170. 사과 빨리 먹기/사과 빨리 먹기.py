import sys
from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
answer = []
apples = 0

def dfs(cy, cx, steps):
    global apples
    if apples == 3:
        answer.append(steps)
    
    for i in range(4):
        y = cy + dy[i]
        x = cx + dx[i]
        if y < 0 or y > 4 or x < 0 or x > 4:
            continue
        
        if board[y][x] == -1:
            continue
        
        if board[y][x] == 1:
            apples += 1
            
        temp = board[cy][cx]
        board[cy][cx] = -1
        dfs(y, x, steps + 1)
        board[cy][cx] = temp
        
        if board[y][x] == 1:
            apples -= 1

board = []
for _ in range(5):
    board.append(list(map(int, sys.stdin.readline().split())))
    
r, c = map(int, sys.stdin.readline().split())
dfs(r, c, 0)

if answer:
    print(min(answer))
else:
    print(-1)