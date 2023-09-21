import sys

def solution():
    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))
        
    for i in range(n-1, 0, -1):
        for j, _ in enumerate(board[i][:-1]):
            board[i-1][j] += max(board[i][j: j + 2])
            
        
    print(board[0][0])
            
        
    

n = int(sys.stdin.readline())
solution()