import sys
from collections import deque

def L(n):
    return n // 1000 + (n % 1000) * 10, "L"

def R(n):
    return  n // 10 + (n % 10) * 1000, "R"

def D(n):
    return (n * 2) % 10000, "D"

def S(n):
    return n - 1 if n != 0 else 9999, "S"

def bfs(start, target):
    queue = deque()
    queue.append((start, ""))
    visited = set()
    visited.add(start)
    
    while queue:
        now, now_status = queue.popleft()
        if now == target:
            return now_status
        
        for function in func:
            next_num, operation = function(now)
            
            if not next_num in visited:
                visited.add(next_num)
                queue.append((next_num, now_status + operation))
                
    return now_status
            
            
T = int(sys.stdin.readline())
func = [D, S, L, R]
for _ in range(T):
    print(bfs(*map(int, sys.stdin.readline().split())))
    # print("".join(result))