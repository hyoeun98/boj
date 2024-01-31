def solution(board, h, w):
    answer = 0
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    length = len(board)
    for i in range(4):
        ny, nx = h + dy[i], w + dx[i]
        if not 0 <= ny < length or not 0 <= nx < length:
            continue
        else:
            if board[h][w] == board[ny][nx]:
                answer += 1
    return answer