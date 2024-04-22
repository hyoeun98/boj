import sys
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [-1 for _ in range(n + 1)]
    visited[start] = 0
    
    while queue:
        current = queue.popleft()
        for next_node, distance in tree[current]:
            if visited[next_node] == -1:
                queue.append(next_node)
                visited[next_node] = visited[current] + distance
                
    m = max(visited)
    return (visited.index(m), m)
    
n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, c, d = map(int,input().split())
    tree[p].append((c, d))
    tree[c].append((p, d))
 
start, _ = bfs(1)
_, answer = bfs(start)
print(answer)
    