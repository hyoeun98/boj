import sys

board = []
for _ in range(10):
    board.append(sys.stdin.readline().strip())
    
a = 0
b = 0
width = [False for _ in range(12)]
height = [False for _ in range(12)]
square = [False for _ in range(9)]
cnt = 0
for i in range(0, 10, 3):
    if board[i][1] == "-":
        width[cnt] = True
    else:
        a += 1
    cnt += 1
    if board[i][4] == "-":
        width[cnt] = True
    else:
        a += 1
    cnt += 1
    if board[i][7] == "-":
        width[cnt] = True
    else:
        a += 1
    cnt += 1
    
temp = [[(i, j) for i in range(1, 10, 3)] for j in range(0, 10, 3)]
cnt = 0
for i in temp:
    for y, x in i:
        if board[y][x] == "|":
            height[cnt] = True
        else:
            a += 1
        cnt += 1

if width[0] and width[3] and height[0] and height[3]:
    b += 1
if width[1] and width[4] and height[3] and height[6]:
    b += 1
if width[2] and width[5] and height[6] and height[9]:
    b += 1
if width[3] and width[6] and height[1] and height[4]:
    b += 1
if width[4] and width[7] and height[4] and height[7]:
    b += 1
if width[5] and width[8] and height[7] and height[10]:
    b += 1
if width[6] and width[9] and height[2] and height[5]:
    b += 1
if width[7] and width[10] and height[5] and height[8]:
    b += 1
if width[8] and width[11] and height[8] and height[11]:
    b += 1
if width[0] and width[1] and width[6] and width[7] and height[0] and height[1] and height[6] and height[7]:
    b += 1
if width[1] and width[2] and width[7] and width[8] and height[3] and height[4] and height[9] and height[10]:
    b += 1
if width[3] and width[4] and width[9] and width[10] and height[1] and height[2] and height[7] and height[8]:
    b += 1
if width[4] and width[5] and width[10] and width[11] and height[4] and height[5] and height[10] and height[11]:
    b += 1
if width[0] and width[1] and width[2] and width[9] and width[10] and width[11] and height[0] and height[1] and height[2] and height[9] and height[10] and height[11]:
    b += 1
    
print(a, b)