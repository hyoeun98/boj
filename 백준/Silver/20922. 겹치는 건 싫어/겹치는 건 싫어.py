import sys
from collections import defaultdict

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

seq = defaultdict(int)
answer = 0
start, end = 0, 0

while end < n:
    if seq[arr[end]] < k:
        seq[arr[end]] += 1
        end += 1
    else:
        seq[arr[start]] -= 1
        start += 1
        
    answer = max(answer, end - start)
    
print(answer)

    