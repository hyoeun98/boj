import sys

n = int(sys.stdin.readline().strip())
coordinate = []
for _ in range(n):
    coordinate.append(list(map(int, sys.stdin.readline().split())))
    
coordinate.sort(key = lambda x: (x[1], x[0]))
for i in coordinate:
    print(*i)