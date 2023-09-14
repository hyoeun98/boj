import sys
from collections import deque
from pprint import pprint

def solution():
    board = [[0, 0, 0]]
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().split()))) # RGB
    
    dp = [[0 for _ in range(3)] for _ in range(n + 1)]
    dp[1] = board[1]

    for i in range(2, n + 1):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + board[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + board[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + board[i][2]
    
    print(min(dp[-1]))
n = int(sys.stdin.readline())
solution()