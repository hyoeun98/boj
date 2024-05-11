import sys

n, k = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    n, g, s, b = map(int, sys.stdin.readline().split())
    arr.append((n, [g, s, b]))
    
arr.sort(key= lambda x: x[1], reverse= True)
for i, v in enumerate(arr):
    if v[0] == k:
        answer = v[1]
        break
    
for i, v in enumerate(arr[:i]):
    if v[1] == answer:
        print(i + 1)
        break
    
else:
    print(i)
    