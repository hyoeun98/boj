import sys    
from collections import deque
def bfs():
    queue = deque()
    queue.append((1, 0))
    visited = [False for _ in range(101)]
    visited[1] = True
    
    while queue:
        currnet, cnt = queue.popleft()
        if currnet == 100:
            return cnt
        for i in range(1, 7):
            next_node = currnet + i
            if next_node > 100 or visited[next_node]:
                continue
            else:
                if next_node in up_down.keys():
                    queue.append((up_down[next_node], cnt + 1))
                elif next_node <= 100:
                    queue.append((next_node, cnt + 1))
                visited[next_node] = True
            
n ,m = map(int, sys.stdin.readline().split())
up_down = dict()
answer = 0
current = 1
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    up_down[x] = y

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    up_down[u] = v


answer = bfs()
print(answer)
