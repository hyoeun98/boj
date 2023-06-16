import sys

def find_parent(x):
    if x == parents[x]:
        return x
    parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    
    if x == y:
        return
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
        
N = int(sys.stdin.readline())
parents = [i for i in range(N)]
stars = [] # x, y
weights = [] # cost, node1, node2
answer = 0

for _ in range(N):
    stars.append(list(map(float, sys.stdin.readline().split())))

for i in range(N-1):
    for j in range(i+1, N):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        weights.append([((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5), i, j])

weights.sort()

for i in weights:
    w, x, y = i
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        answer += w

print(answer)
