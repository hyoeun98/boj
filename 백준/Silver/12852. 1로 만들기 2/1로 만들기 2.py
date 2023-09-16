import sys
from collections import deque
def solution():
    queue = deque()
    queue.append([n])
    visited = set()
    while queue:
        arr = queue.popleft()
        num = arr[-1]
        # print(arr, num)
        if num == 1:
            print(len(arr) - 1)
            print(*arr)
            break
        if num % 3 == 0 and (num // 3) not in visited:
            queue.append(arr + [num // 3])
            visited.add(num // 3)
        if num % 2 == 0 and (num // 2) not in visited:
            queue.append(arr + [num // 2])
            visited.add(num // 2)
        if (num - 1) not in visited:
            queue.append(arr + [num - 1])
            visited.add(num - 1)
    
    
n = int(sys.stdin.readline())
solution()