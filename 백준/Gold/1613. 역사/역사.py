import sys

def floydwarshall():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):    
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
n, k = map(int, sys.stdin.readline().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    
floydwarshall()

# print(graph)
s = int(sys.stdin.readline())
for _ in range(s):
    a, b = map(int, sys.stdin.readline().split())
    if graph[a][b] == 1:
        print(-1)
    elif graph[b][a] == 1:
        print(1)
    else:
        print(0)
