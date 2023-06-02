import sys
sys.setrecursionlimit(100000000)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N+1)]

for i in range(M):
    flag, a, b = map(int, sys.stdin.readline().split())
    if flag == 0:
        union(a,b)
    else:
        parent_a = find(a)
        parent_b = find(b)
        if parent_a == parent_b:
            print('YES')
        else:
            print('NO')