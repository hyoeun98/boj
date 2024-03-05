import sys
from collections import deque
n = int(sys.stdin.readline())

arr = deque(range(1, n + 1))

while len(arr) > 1:
    del arr[0]
    arr.rotate(-1)
    
print(arr[0])