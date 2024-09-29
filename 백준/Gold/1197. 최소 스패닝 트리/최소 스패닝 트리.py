import sys
from heapq import heappop, heappush

v, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
answer = 0
queue = [[0, 1]]
visited = set()

while len(visited) < v:
    weight, vertex = heappop(queue)
    if vertex not in visited:
        visited.add(vertex)
        answer += weight
        for i, j in graph[vertex]:
            heappush(queue, (j, i))
print(answer)
    
