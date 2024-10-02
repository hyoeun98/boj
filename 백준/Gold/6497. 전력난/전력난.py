import sys
from heapq import heappop, heappush

while True:
    m, n = map(int, sys.stdin.readline().split())
    if m == 0 and n == 0:
        break 
    graph = [[] for _ in range(m)]
    sum_of_price = 0
    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        graph[x].append((y, z))
        graph[y].append((x, z))
        sum_of_price += z
        
    queue = []
    queue.append((0, 0)) # weight, node
    answer = 0
    visited = set()

    while len(visited) < m:
        weight, vertex = heappop(queue)
        if vertex not in visited:
            answer += weight
            visited.add(vertex)
            for n_vertex, n_weight in graph[vertex]:
                if n_vertex not in visited:
                    heappush(queue, (n_weight, n_vertex))
            
    print(sum_of_price - answer)

