import sys

def solution():
    if n <= 2:
        print(1)
        return
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    print(dp[-1])
n = int(sys.stdin.readline())
solution()