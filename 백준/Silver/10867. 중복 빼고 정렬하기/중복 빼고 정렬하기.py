import sys

n = int(sys.stdin.readline().strip())
arr = list(set(map(int, sys.stdin.readline().split())))
    
arr.sort()
print(*arr)