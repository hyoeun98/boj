import sys

def check(i, j):
    temp = 0
    if n - i >= 4:
        temp = max(temp, board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j])
    if m - j >= 4:
        temp = max(temp, sum(board[i][j:j+4]))
    if n - i >= 2 and m - j >= 2:
        temp = max(temp, sum(board[i][j:j+2]) + sum(board[i+1][j:j+2]))
    if n - i >= 3 and m - j >= 2:
        temp = max(temp, board[i][j] + board[i+1][j] + sum(board[i+2][j:j+2]))
    if n - i >= 2 and m - j >= 3:
        temp = max(temp, sum(board[i][j:j+3]) + board[i+1][j])
    if n - i >= 3 and m - j >= 2:
        temp = max(temp, sum(board[i][j:j+2]) + board[i+1][j+1] + board[i+2][j+1])
    if n - i >= 2 and j >= 2:
        temp = max(temp, board[i][j] + sum(board[i+1][j-2:j+1]))
    if n - i >= 3 and m - j >= 2:
        temp = max(temp, board[i][j] + sum(board[i+1][j:j+2]) + board[i+2][j+1])
    if n - i >= 2 and j >= 1 and m - j >= 2:
        temp = max(temp, sum(board[i][j:j+2]) + sum(board[i+1][j-1:j+1]))
    if n - i >= 2 and m - j >= 3:
        temp = max(temp, sum(board[i][j:j+2]) + sum(board[i+1][j+1:j+3]))
    if n - i >= 3 and j >= 1:
        temp = max(temp, board[i][j] + sum(board[i+1][j-1:j+1]) + board[i+2][j-1])
    if n - i >= 3 and m - j >= 2:
        temp = max(temp, sum(board[i][j:j+2]) + board[i+1][j] + board[i+2][j])
    if n - i >= 3 and j >= 1:
        temp = max(temp, board[i][j] + board[i+1][j] + sum(board[i+2][j-1:j+1]))
    if n - i >= 2 and m - j >= 3:
        temp = max(temp, sum(board[i][j:j+3]) + board[i+1][j+2])
    if n - i >= 2 and m - j >= 3:
        temp = max(temp, board[i][j] + sum(board[i+1][j:j+3]))
    if n - i >= 2 and m - j >= 3:
        temp = max(temp, sum(board[i][j:j+3]) + board[i+1][j+1])
    if n - i >= 3 and j >= 1:
        temp = max(temp, board[i][j] + sum(board[i+1][j-1:j+1]) + board[i+2][j])
    if n - i >= 2 and j >= 1 and m - j >= 2:
        temp = max(temp, board[i][j] + sum(board[i+1][j-1:j+2]))
    if n - i >= 3 and m - j >= 2:
        temp = max(temp, board[i][j] + sum(board[i+1][j:j+2]) + board[i+2][j])
    
    return temp
n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
    
answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, check(i, j))
print(answer)
    
    
