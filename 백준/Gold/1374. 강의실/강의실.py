import sys
from heapq import heappop, heappush
n = int(sys.stdin.readline())

arr = []
answer = 0
for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    arr.append((b, c))

heap = []
arr.sort()
for start, end in arr:
    while heap and heap[0] <= start:
        heappop(heap)
    heappush(heap, end)
    answer = max(answer, len(heap))
print(answer)
    