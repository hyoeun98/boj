from re import L
import sys
def move(y, x, direction):
    if direction == 1:
        if y + 1 < r and board[y + 1][x] == -1:
            return (y + 1, x, 1)
        else:
            return (y, x + 1, 2)
    elif direction == 2:
        if x + 1 < c and board[y][x + 1] == -1:
            return (y, x + 1, 2)
        else:
            return (y - 1, x, 3)
    elif direction == 3:
        if y > 0 and board[y - 1][x] == -1:
            return (y - 1, x, 3)
        else:
            return (y, x - 1, 4)
    else:
        if x > 0 and board[y][x - 1] == -1:
            return (y, x - 1, 4)
        else:
            return (y + 1, x, 1)
    
c, r = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
if c * r < k:
    print(0)
    exit()
elif k == 1:
    print(1, 1)
    exit()
elif k == 2:
    print(1, 2)
    exit()
board = [[-1 for _ in range(c)] for _ in range(r)]
board[0][0] = 1
cnt = 2
y, x, direction = move(0, 0, 1)
while cnt < c * r:
    board[y][x] = cnt
    cnt += 1
    y, x, direction = move(y, x, direction)
    if cnt == k:
        print(x + 1, y + 1)
        break



