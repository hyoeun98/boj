import sys
            
def solution():
    N, M  = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    construct = []
    for _ in range(K):
        a, b, c, d = map(int, sys.stdin.readline().split())
        if a > c:
            c, a = a, c
        elif b > d:
            d, b = b, d
            
        construct.append((b, a, d, c))
        
    dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
    
    for i in range(M + 1):
        if (i - 1, 0, i, 0) in construct:
            break
        dp[i][0] = 1
        
    for i in range(N + 1):
        if (0, i - 1, 0, i) in construct:
            break
        dp[0][i] = 1
    
    
    # print(dp)
    for j in range(1, N + 1):
        for i in range(1, M + 1):
            if (i - 1, j, i, j) in construct:
                col = 0
            else:
                col = dp[i - 1][j]
            
            if (i, j - 1, i, j) in construct:
                row = 0
            else:
                row = dp[i][j - 1]
                
            dp[i][j] = row + col
    print(dp[M][N])

solution()
        