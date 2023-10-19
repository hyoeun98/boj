import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append(n)
    moving = [lambda x: x * 2, lambda x: x + 1, lambda x: x - 1]
    visited = [[-1, 100001] for _ in range(100001)] # 이전 node, elapsed time
    visited[n][0] = n
    visited[n][1] = 0

    while queue:
        current = queue.popleft()
        
        if current == k:
            return visited
        for i in moving:
            next_point = i(current)
            if next_point < 0 or next_point> 100000:
                continue
            elif visited[next_point][0] == -1 or visited[next_point][1] > visited[current][1] + 1:
                visited[next_point][0] = current
                visited[next_point][1] = visited[current][1] + 1
                queue.append(next_point)
    return visited

def solution():
    route = bfs()
    start = k
    cnt = 0
    arr = [k]
    while start != n:
        arr.append(route[start][0])
        start = route[start][0]
        cnt += 1
    print(cnt)
    print(*reversed(arr))
n, k = map(int ,sys.stdin.readline().split())
solution()

