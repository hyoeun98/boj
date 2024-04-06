import sys
import heapq as hq


def dk(start):
    queue = []
    hq.heappush(queue, (start, 0))
    distance = [1e9 for _ in range(n + 1)]
    distance[start] = 0 
    
    while queue:
        current, dist = hq.heappop(queue)
        
        if distance[current] < dist:
            continue
        
        for i in board[current]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist +i[1]
                hq.heappush(queue, (i[0], dist + i[1]))
    
    return distance # start에서 다른 node까지의 distance

n, m, x = map(int, sys.stdin.readline().split())
board = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().split())
    board[a].append((b, t))
    
answer = dk(x)
for i in range(1, n + 1):
    if i == x:
        continue
    temp = dk(i)
    answer[i] += temp[x]
    
print(max(answer[1:]))