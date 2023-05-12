def solution(board, k):
    answer = 0
    for i, v in enumerate(board):
        for j, _ in enumerate(board[0]):
            if i + j <= k:
                answer += board[i][j]    
    return answer