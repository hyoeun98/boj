import sys
from heapq import heappop, heappush
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

answer = 0
visited = set()
queue = []
queue.append((0, 0))
while len(visited) < n:
    weight, vertex = heappop(queue)
    if vertex not in visited:
        answer += weight
        visited.add(vertex)
        for i, v in enumerate(arr[vertex]):
            if i not in visited:
                heappush(queue, ((v, i)))
                
print(answer)