import sys
from collections import deque

def solution():
    arr = []
    for _ in range(n):
        arr.append(int(sys.stdin.readline()))
    
    arr.sort()
    for i in arr:
        print(i)
n = int(sys.stdin.readline())
solution()