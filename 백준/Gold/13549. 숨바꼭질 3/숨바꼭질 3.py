import sys
from collections import deque

def solution():
    queue = deque()
    queue.append((n, 0))
    visited = [-1 for _ in range(100001)]
    visited[n] = 0
    while queue:
        x, time = queue.popleft()
        # print(x, time)
        if x == k:
            print(time)
            return

        temp = x

        while temp !=0 and temp <= 100000:
            if visited[temp] == -1 or visited[temp] > time:
                visited[temp] = time
                queue.append((temp, time))
            temp *= 2
        
        if x != 0:
            if visited[x - 1] == -1 or visited[x - 1] > time:
                visited[x - 1] = time + 1
                queue.append((x - 1, time + 1))
        if x != 100000:
            if visited[x + 1] == -1 or visited[x + 1] > time:
                visited[x + 1] = time + 1
                queue.append((x + 1, time + 1))
            
n, k = map(int, sys.stdin.readline().split())
solution()