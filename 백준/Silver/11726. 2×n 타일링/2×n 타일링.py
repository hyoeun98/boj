import sys

def solution():
    
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[-1]%10007)
n = int(sys.stdin.readline())
if n <= 3:
    print(n)
else:
    solution()