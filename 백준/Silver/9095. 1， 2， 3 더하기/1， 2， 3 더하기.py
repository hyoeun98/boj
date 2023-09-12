import sys
from collections import deque

def solution():
    n = int(sys.stdin.readline())    
    dp = [0 for _ in range(12)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[n])

T = int(sys.stdin.readline())
for _ in range(T):
    solution()