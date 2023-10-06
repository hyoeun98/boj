import sys

T = int(sys.stdin.readline().strip())

def solution():
    n = int(sys.stdin.readline().strip())
    sticker = []
    dp = [[0 for _ in range(n)] for _ in range(2)]
    
    for _ in range(2):
        sticker.append(list(map(int, sys.stdin.readline().split())))
    
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    if n > 1:
        dp[0][1] = dp[1][0] + sticker[0][1]
        dp[1][1] = dp[0][0] + sticker[1][1]
        
    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + sticker[1][i]
        
    print(max(dp[0][-1], dp[1][-1]))
for _ in range(T):
    solution()
        