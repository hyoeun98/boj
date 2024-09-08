import sys

r, c = map(int, sys.stdin.readline().split())
board = []
for _ in range(r):
    board.append(list(sys.stdin.readline().strip()))
    
land = []
for i in range(r):
    for j in range(c):
        if board[i][j] == "X":
            land.append((i, j))
        
for y, x in land[:]:
    cnt = 0
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        cy ,cx = y + dy, x + dx
        if 0 <= cy < r and 0 <= cx < c:
            if board[cy][cx] == ".":
                cnt += 1
        else:
            cnt += 1
            
    if cnt >= 3:
        land.remove((y, x))

moderate_y = min([i[0] for i in land])
moderate_x = min([i[1] for i in land])

for i, v in enumerate(land):
    land[i] = land[i][0] - moderate_y, land[i][1] - moderate_x
    
answer = [["."] * (max([i[1] for i in land]) + 1) for _ in range(max([i[0] for i in land]) + 1)]
for y, x in land:
    answer[y][x] = "X"

for i in answer:
    print("".join(i))