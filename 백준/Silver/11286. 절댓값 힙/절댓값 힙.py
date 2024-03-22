import sys    
import heapq
n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    op = int(sys.stdin.readline())
    if op == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, (abs(op), op))
