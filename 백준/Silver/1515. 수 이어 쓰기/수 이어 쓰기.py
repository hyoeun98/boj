import sys

n = list(sys.stdin.readline().strip())
for i in range(1, 30000):
    for j in str(i):
        if n and j == n[0]:
            del n[0]
    
    if not n:
        print(i)
        break
