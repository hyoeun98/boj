import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
arr = deque(arr)
answer = 0
a, b = 0, 0
for i in range(k):
    if i % 2 == 0:
        a = arr.pop()
        answer += a - b
    else:
        b = arr.popleft()
print(answer)
