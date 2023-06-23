import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
coins = []
answer = []

for _ in range(n):
    coins.append(int(sys.stdin.readline()))
coins.sort()

# dp = [[] for _ in range(n)]
dp = [1 if i % coins[0] == 0 else 0 for i in range(k+1)]
for i in coins[1:]:
    for dp_idx, j in enumerate(dp):
        if dp_idx < i:
            continue
        dp[dp_idx] = j + dp[dp_idx - i]

print(dp[-1])