import sys
from collections import deque
    
def solution():
    dp = [0 for _ in range(F + 1)]
    queue = deque()
    queue.append(S)
    visited = set()
    visited.add(S)
    while queue:
        current = queue.popleft()
        
        if current == G:
            print(dp[current])
            return
        
        if current + U <= F and (current + U) not in visited:
            queue.append(current + U)
            dp[current + U] = dp[current] + 1
            visited.add(current + U)
        if current - D >= 1 and (current - D) not in visited:
            queue.append(current - D)
            dp[current - D] = dp[current] + 1
            visited.add(current - D)

    print("use the stairs")
F, S, G, U, D= map(int, sys.stdin.readline().split())

solution()


