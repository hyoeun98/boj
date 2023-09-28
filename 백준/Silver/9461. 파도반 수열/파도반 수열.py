import sys
from collections import deque

def solution():
    n = int(sys.stdin.readline())
    if n <= 3:
        print(1)
        return
    dp = [0 for _ in range(n)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n):
        dp[i] = dp[i - 2] + dp[i - 3]
    
    print(dp[-1])
t = int(sys.stdin.readline())
for _ in range(t):
    solution()