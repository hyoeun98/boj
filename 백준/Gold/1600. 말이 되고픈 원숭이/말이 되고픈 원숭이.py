import sys
from collections import deque
from pprint import pprint
def bfs(board):
    global k, w, h
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    hy = [2, 2, 1, 1, -1, -1, -2 ,-2]
    hx = [1, -1, 2, -2, 2, -2, 1, -1]

    queue = deque()
    queue.append((0, 0, k))
    visited = [[[-1 for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]
    for i in range(k + 1):
        visited[0][0][i] = 0

    while queue:
        y, x, remain_k = queue.popleft()
        # print(y, x, remain_k)
        if y == h - 1 and x == w - 1:
            # pprint(visited)
            answer = min(visited[y][x]) if min(visited[y][x]) != -1 else max(visited[y][x])
            print(answer)
            return
        if remain_k > 0: # k가 남아 있을 경우
             for i in range(8):
                ny, nx = y + hy[i], x + hx[i]
                if not (0 <= ny < h and 0 <= nx < w):
                    continue
                if board[ny][nx] != 1 and (visited[ny][nx][remain_k - 1] == -1):
                    visited[ny][nx][remain_k - 1] = visited[y][x][remain_k] + 1
                    queue.append((ny, nx, remain_k - 1))

        for i in range(4):
            ny, nx = y +dy[i], x + dx[i]
            if not (0 <= ny < h and 0 <= nx < w):
                continue
            if board[ny][nx] != 1 and (visited[ny][nx][remain_k] == -1):
                visited[ny][nx][remain_k] = visited[y][x][remain_k] + 1
                queue.append((ny, nx, remain_k))

    print(-1)
def solution():
    board = []
    for _ in range(h):
        board.append(list(map(int, sys.stdin.readline().split())))
    bfs(board)

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())

solution()