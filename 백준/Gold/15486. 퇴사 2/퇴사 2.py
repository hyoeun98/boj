import sys

N = int(sys.stdin.readline())
T, P = [], []
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)
for i in range(N-1, -1, -1):
    if i + T[i] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i] + dp[i+T[i]])
    
print(max(dp))
