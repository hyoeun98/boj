import sys
from collections import deque

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

def bfs():
    queue = deque()
    visited = set()
    queue.append((a, 0))
    visited.add(a)
    
    while queue:
        current, cnt = queue.popleft()
        if current == b:
            print(cnt)
            break
        int_current = int(current, 2)
        plus = bin(int_current + 1)[2:]
        minus = bin(int_current - 1)[2:]
        if plus not in visited:
            queue.append((plus, cnt + 1))
            visited.add(plus)
        if current != "0" and minus not in visited:
            queue.append((minus, cnt + 1))
            visited.add(minus)
            
        for i in range(len(current) - 1):
            temp = bin(int_current^(1 << i))[2:]
            if temp not in visited:
                queue.append((temp, cnt + 1))
                visited.add(temp)   
bfs()