import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
board = [[1e9 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    board[a][b] = min(board[a][b], c)
    
for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            if j != k:
                board[j][k] = min(board[j][k], board[j][i] + board[i][k])

for i in board[1:]:
    for j in i[1:]:
        print(j if j != 1e9 else 0, end = " ")
    print()