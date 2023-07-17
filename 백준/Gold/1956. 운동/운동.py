import sys

def solution():
    V, E = map(int, sys.stdin.readline().split())
    graph = [[10e9 for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a][b] = c
    
    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    answer = 10e9
    for i in range(1, V + 1):
        answer = min(answer, graph[i][i])

    print(answer if answer != 10e9 else -1)
    

solution()