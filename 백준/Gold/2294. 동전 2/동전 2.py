import sys
from collections import deque
            
n, k = map(int, sys.stdin.readline().split())
coins = set()
for _ in range(n):
    coins.add(int(sys.stdin.readline()))
    
coins = list(coins)
coins.sort()

dp = [10001 for _ in range(k+1)]
dp[0] = 0

for i in range(1,k+1):
    for coin in coins:
        if i < coin:
            break
        else:
            dp[i] = min(dp[i-coin]+1,dp[i])

print(-1 if dp[k]==10001 else dp[k])


