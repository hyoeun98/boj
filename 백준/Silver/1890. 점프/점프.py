import sys
from pprint import pprint
N = int(sys.stdin.readline().strip())

def solution():
    board = []
    for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1
    for y in range(N):
        for x in range(N):
            if y == N - 1 and x == N - 1:
                break
            if x + board[y][x] < N:
                dp[y][x + board[y][x]] += dp[y][x]
            if y + board[y][x] < N:
                dp[y + board[y][x]][x] += dp[y][x]
    
    print(dp[N - 1][N - 1])

solution()