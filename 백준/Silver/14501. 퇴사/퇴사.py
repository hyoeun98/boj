import sys

N = int(sys.stdin.readline().strip())

def solution():
    counseling = []
    dp = [0 for _ in range(N + 1)]
    for _ in range(N):
        counseling.append(list(map(int, sys.stdin.readline().split())))
    
    for i in range(N):
        for j in range(i + counseling[i][0], N + 1):
            if dp[j] < dp[i] + counseling[i][1]:
                dp[j] = dp[i] + counseling[i][1]
            
    
    # print(dp)
    print(dp[-1])
solution()
        