import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    answer = 0
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    top = arr.pop()
    stack = deque()
    stack.append(top)
    for i in reversed(arr):
        if i < top:
            answer += top - i
        elif i > top:
            top = i
    
    print(answer)
    
    