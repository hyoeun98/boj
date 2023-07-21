import sys
import pprint
ppr = pprint.pprint

def solution():
    N, K = map(int, sys.stdin.readline().split())
    arr = [[0, 0]]
    for _ in range(N): 
        arr.append(list(map(int, sys.stdin.readline().split())))
    
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        weight, value = arr[i]
        for j in range(1, K + 1): # 현재 무게
            
            if j < weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            # print(weight, value, i, j)
            # ppr(dp)
            
            
    
    print(dp[N][K])
    
solution()