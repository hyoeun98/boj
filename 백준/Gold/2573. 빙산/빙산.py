import sys
from collections import deque
from pprint import pprint
ppr = pprint
                
def bfs(y, x, visited):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
        
    queue = deque()
    queue.append((y, x))
    temp = []
    
    while queue:
        y, x = queue.popleft()
        visited.add((y, x))
        num_sea = 0
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if board[ny][nx] == 0:
                num_sea += 1
            elif (ny, nx) not in visited and (ny, nx) not in queue:
                queue.append((ny, nx))
                
        
        temp.append([y, x, max(0, board[y][x] - num_sea)])
            
    for y, x, r in temp:
         board[y][x] = r

    return 1

def solution():
    answer = 0
    while True:
        visited = set()
        cnt = 0
        ice = []
        for i in range(n):
            for j in range(m):
                if board[i][j] != 0: 
                    ice.append((i,j))
                    
        if len(ice) <= 1:
            print(0)
            break
        
        for y, x in ice:
            if (y, x) not in visited:
                cnt += bfs(y, x, visited)
        
        # ppr(board)
        if cnt > 1:
            print(answer)
            break
        answer += 1
        
    
    
    
n ,m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
    
solution()
        