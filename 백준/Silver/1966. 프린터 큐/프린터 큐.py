import sys
from collections import deque

def solution():
    cnt = 0
    while sum(valid):
        if arr[0] >= max(arr):
            del arr[0]
            del valid[0]
            cnt += 1
        else:
            arr.rotate(-1)
            valid.rotate(-1)
            
    
    print(cnt)
    
k = int(sys.stdin.readline())

for _ in range(k):
    n, m = map(int, sys.stdin.readline().split())
    arr = deque(map(int, sys.stdin.readline().split()))
    valid = deque([1 if i == m else 0 for i, v in enumerate(arr)])
    solution()
    

