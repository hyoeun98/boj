def solution(board):
    answer = 0
    n = len(board)
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 0, 1, -1 ,0 ,1 ,-1]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 0:
                        board[x][y] = 2
    for i in board:
        for j in i:
            if j == 0:
                answer += 1
    return answer