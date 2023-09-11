import sys
from collections import deque
from pprint import pprint

dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]

def bfs(board, queue, visited, fire_visited):
    while queue:
        y, x, obj = queue.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if not (0 <= ny < h and 0 <= nx < w) or board[ny][nx] == "#":
                continue
            if obj == "fire" and not fire_visited[ny][nx]:
                queue.append((ny, nx, obj))
                fire_visited[ny][nx] = 1
            elif obj == "human" and not visited[ny][nx] and not fire_visited[ny][nx]:
                queue.append((ny, nx, obj))
                visited[ny][nx] = visited[y][x] + 1
    # pprint(visited)

def solution():
    board = []
    for _ in range(h):
        board.append(list(sys.stdin.readline().strip()))

    queue = deque()
    visited = [[0 for _ in range(w)] for _ in range(h)]
    fire_visited = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j] == "@":
                human = (i, j, "human")
                visited[i][j] = 1
            elif board[i][j] == "*":
                queue.append((i, j, "fire"))
                fire_visited[i][j] = 1
                

    queue.append(human)
    bfs(board, queue, visited, fire_visited)
    candidate = []
    for i in range(h):
        for j in range(w):
            if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                if visited[i][j] != 0:
                    candidate.append(visited[i][j])
    candidate.sort()
    print(candidate[0] if candidate else "IMPOSSIBLE")
t = int(sys.stdin.readline())
for _ in range(t):
    w, h = map(int, sys.stdin.readline().split())
    solution()