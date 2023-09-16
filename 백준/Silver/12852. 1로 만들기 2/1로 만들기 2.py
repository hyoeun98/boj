import sys
from collections import deque
def solution():
    dp = [[[], 0] for _ in range(n + 1)]
    dp[1][0] = [1]
    dp[1][1] = 0

    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][0] + [i]
        dp[i][1] = dp[i - 1][1] + 1

        if i % 2 == 0:
            if dp[i][1] > dp[i // 2][1] + 1:
                dp[i][0] = dp[i // 2][0] + [i]
                dp[i][1] = dp[i // 2][1] + 1
    
        if i % 3 == 0:
            if dp[i][1] > dp[i // 3][1] + 1:
                dp[i][0] = dp[i // 3][0] + [i]
                dp[i][1] = dp[i // 3][1] + 1

    print(dp[-1][1])
    print(*dp[-1][0][::-1])
n = int(sys.stdin.readline())
solution()