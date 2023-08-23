import sys

def solution():
    answer = 0
    graph = [[True for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    if road[j][k] == road[j][i] + road[i][k]:
                        graph[j][k] = False
                    elif road[j][k] > road[j][i] + road[i][k]:
                        print(-1)
                        return
    for i in range(n):
        for j in range(i, n):
            if graph[i][j]:
                answer += road[i][j]
    print(answer)

n = int(sys.stdin.readline())
road = []
for _ in range(n):
    road.append(list(map(int, sys.stdin.readline().split())))

solution()
