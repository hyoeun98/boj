import sys
from collections import deque

def bfs(M, N, tomato, is_tomato):
    answer = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while is_tomato:
        y, x = is_tomato.popleft()
        for i in range(4):
            row, col = y + dy[i], x + dx[i]
            if 0 <= row < N and 0 <= col < M and tomato[row][col] == 0:
                tomato[row][col] = tomato[y][x] + 1
                is_tomato.append((row, col))

    for i in tomato:
        for j in i:
            if j == 0:
                print(-1)
                return
        answer = max(answer, max(i))

    print(answer - 1)
    
def solution():
    M, N = map(int, sys.stdin.readline().split())
    tomato = []
    for _ in range(N):
        tomato.append(list(map(int, sys.stdin.readline().split())))

    is_tomato = deque()
    for row, i in enumerate(tomato):
        for col, j in enumerate(i):
            if j == 1:
                is_tomato.append((row, col))

    bfs(M, N, tomato, is_tomato)

solution()

