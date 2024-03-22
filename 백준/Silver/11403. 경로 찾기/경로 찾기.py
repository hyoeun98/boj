import sys    

n = int(sys.stdin.readline())
board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
    
for i in range(n):
    for j in range(n):
        for k in range(n):
            if board[j][i] and board[i][k]:
                board[j][k] = 1
    
for i in board:
    print(*i)
