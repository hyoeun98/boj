import sys

def solution():
    n = int(sys.stdin.readline())
    dp = [[0, 0] for _ in range(n + 2)]
    dp[0] = [1, 0]
    dp[1] = [0, 1]

    for i in range(2, n + 1):
        dp[i] = dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1] 
    
    print(*dp[n])

T = int(sys.stdin.readline())
for _ in range(T):
    solution()