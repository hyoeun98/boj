import sys
from collections import deque
from heapq import heappush, heappop

n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
visited = set()

answer = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
queue = []
queue.append((0, 1))
max_weight = 0
while len(visited) < n:
    weight, vertex = heappop(queue)
    if vertex not in visited:
        max_weight = max(max_weight, weight)
        visited.add(vertex)
        answer += weight
        for next_vertex, next_weight in graph[vertex]:
            if next_vertex not in visited:
                heappush(queue, (next_weight, next_vertex))
        
print(answer - max_weight)
