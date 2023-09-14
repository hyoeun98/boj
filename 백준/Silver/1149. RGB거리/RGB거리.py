import sys

n = int(sys.stdin.readline())
dp = [[0 for _ in range(3)] for _ in range(n + 1)]
dp[1][0], dp[1][1], dp[1][2] = map(int, sys.stdin.readline().split())

for i in range(2, n + 1):
    r, g, b = map(int, sys.stdin.readline().split())
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + r
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + g
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + b
    
print(min(dp[-1]))

