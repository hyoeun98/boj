import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    arr.append([int(age), name])
    
arr.sort(key = lambda x: x[0])
for i in arr:
    print(i[0], i[1])