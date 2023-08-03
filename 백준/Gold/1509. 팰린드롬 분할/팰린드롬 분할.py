import sys
import math

def solution():
    seq = sys.stdin.readline().strip()
    n = len(seq)
    
    dp = [[0 if i != j else 1 for i in range(n + 1)] for j in range(n + 1)]
    result = [3000 for _ in range(n + 1)]
    result[0] = 0
    
    for i in range(1, n):
        if seq[i] == seq[i - 1]:
            dp[i][i + 1] = 1
    
    for j in range(2, n):
        for i in range(1, n + 1 - j):
            if seq[i - 1] == seq[i + j - 1] and dp[i + 1][i + j - 1] == 1:
                dp[i][i + j] = 1
                
    for i in range(1, n + 1):
        result[i] = min(result[i], result[i - 1] + 1)
        
        for j in range(i + 1, n + 1):
            if dp[i][j] != 0:
                result[j] = min(result[j], result[i - 1] + 1)
                
    print(result[n])
solution()
        