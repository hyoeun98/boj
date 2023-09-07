import sys
from collections import deque

def solution(board):
    if current == arrive:
        print(0)
        return

    answer = 0
    dy = [1, 1, -1, -1, 2, 2, -2, -2]
    dx = [2, -2, 2, -2, 1, -1, 1, -1]
    queue = deque()
    queue.append(current)
    visited = set()
    a, b = arrive
    
    while queue:
        y, x = queue.popleft()
        visited.add((y, x))
        answer += 1
        for k in range(8):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < l and 0 <= nx < l:
                if ny == a and nx == b:
                    print(board[y][x] + 1)
                    return
                elif (ny, nx) not in visited:
                    queue.append((ny, nx))
                    visited.add((ny, nx))
                    board[ny][nx] = board[y][x] + 1

T = int(sys.stdin.readline())
for _ in range(T):
    l = int(sys.stdin.readline())
    board = [[0 for _ in range(l)] for _ in range(l)]
    current = list(map(int, sys.stdin.readline().split()))
    arrive = list(map(int, sys.stdin.readline().split()))
    solution(board)


