from collections import deque

def solution(board):
    n = len(board)
    cost_map = [[[int(1e7) for _ in range(n)] for _ in range(n)] for _ in range(4)]
    for i in range(4):
        cost_map[i][0][0] = 0
    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)
    
    queue = deque()
    queue.append((0, 0, 0, -1)) # x, y, cost, dir;
    
    while queue:
        x, y, last_cost, last_dir = queue.popleft()
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if 0 > temp_x or 0 > temp_y or temp_y >= n or temp_x >= n:
                continue
            
            if board[temp_x][temp_y] == 1:
                continue
                
            ### cost 계산
            if last_dir == -1 or last_dir == i:
                temp_cost = last_cost + 100
            else:
                temp_cost = last_cost + 600
            ### cost 계산
                
            if temp_cost < cost_map[i][temp_x][temp_y]:
                cost_map[i][temp_x][temp_y] = temp_cost 
                queue.append((temp_x, temp_y, temp_cost, i))
    answer = int(1e8)
    for i in range(4):
        answer = min(answer, cost_map[i][n-1][n-1])
    return answer
