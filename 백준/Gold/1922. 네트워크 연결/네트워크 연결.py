import sys
from heapq import heappop, heappush
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
visited = set()
queue = []
answer = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
queue.append((0, 1))
while len(visited) < n:
    weight, vertex = heappop(queue)
    if vertex not in visited:
        answer += weight
        visited.add(vertex)
        for n_vertex, n_weight in graph[vertex]:
            if n_vertex not in visited:
                heappush(queue, (n_weight, n_vertex))
print(answer)