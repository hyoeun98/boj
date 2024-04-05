import sys
from collections import deque
import pprint
n ,m, r = map(int, sys.stdin.readline().split()) # 지역의 개수, 수색 범위, 길의 개수
t = [0] + list(map(int, sys.stdin.readline().split()))
distance = [[1e9 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    distance[i][i] = 0
    
for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    distance[a][b] = l
    distance[b][a] = l

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if distance[j][k] > distance[j][i] + distance[i][k]:
                distance[j][k] = distance[j][i] + distance[i][k]

answer = 0          
for i in range(1, n + 1):
    temp = 0       
    for j, v in enumerate(distance[i]):
        if v <= m:
            temp += t[j]
    answer = max(answer, temp)
print(answer)
