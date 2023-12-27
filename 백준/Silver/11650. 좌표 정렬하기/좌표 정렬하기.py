import sys

n = int(sys.stdin.readline().strip())
coordinate = []
for _ in range(n):
    coordinate.append(list(map(int, sys.stdin.readline().split())))
    
coordinate.sort()

for i in coordinate:
    print(*i)