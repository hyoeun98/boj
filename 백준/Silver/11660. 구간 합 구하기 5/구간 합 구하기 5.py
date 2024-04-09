import sys

def solve(x1, y1, x2, y2):
    answer = 0
    for i in range(x1, x2 + 1):
        answer += board[i][y2] - board[i][y1-1]
    
    print(answer)
n, m = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(n+1)]]
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for i in range(n - 1):
        temp[i + 1] = temp[i] + temp[i + 1]
    board.append([0] + temp)

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    solve(x1, y1, x2, y2)