import sys
import itertools as it
N, M = map(int, sys.stdin.readline().split())
jewel = []
for _ in range(N):
    jewel.append(int(sys.stdin.readline()))


dp = [0] * (N + 1)
prefix_sum = list(it.accumulate(jewel))
max_sum, min_sum = 0, 0

for i in range(M, N+1):
    max_sum = max(prefix_sum[i-1] - min_sum, max_sum)
    min_sum = min(prefix_sum[i-M], min_sum)
print(max_sum)