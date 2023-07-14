import sys

def solution():
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    dp = [[0] * (K+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1
        dp[i][1] = i

    # print(dp)
    for i in range(2 ,N+1):
        for j in range(2, K+1):
            dp[i][j] = dp[i-2][j-1] + dp[i-1][j]

    # print(dp)
    print((dp[N-3][K-1] + dp[N-1][K]) % 1_000_000_003)

solution()

