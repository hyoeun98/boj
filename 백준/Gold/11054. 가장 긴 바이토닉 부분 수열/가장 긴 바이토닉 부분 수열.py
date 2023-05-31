import sys
from collections import deque
            
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
reversed_A = list(reversed(A))

dp = [1] * N
reversed_dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(N):
    for j in range(i):
        if reversed_A[i] > reversed_A[j]:
            reversed_dp[i] = max(reversed_dp[i], reversed_dp[j] + 1)

answer = [dp[i] + reversed_dp[::-1][i] for i in range(N)]
print(max(answer) - 1)
