import sys
from collections import deque
import copy
def bfs(board, i, j, color):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    queue = deque()
    queue.append((i, j))
    visited = set()
    visited.add((i, j))
    board[i][j] = 0

    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if (ny, nx) not in visited and 0 <= ny < n and 0 <= nx < n and board[ny][nx] == color:
                queue.append((ny, nx))
                board[ny][nx] = 0

def solution():
    board = []
    for _ in range(n):
        board.append(list(sys.stdin.readline().strip()))
    
    answer = [0, 0]
    cpy_board = copy.deepcopy(board)
    for i in range(n):
        for j in range(n):
            if cpy_board[i][j] != 0:
                answer[0] += 1
                bfs(cpy_board, i, j, cpy_board[i][j])

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'G':
                board[i][j] = 'R'
    
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                answer[1] += 1
                bfs(board, i, j, board[i][j])
    print(*answer)
n = int(sys.stdin.readline())

solution()


