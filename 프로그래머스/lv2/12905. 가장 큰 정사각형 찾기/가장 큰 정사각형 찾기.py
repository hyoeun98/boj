def solution(board):
    answer = 0
    map = [m for m in board]
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if col != 0:
                if row_idx == 0 or col_idx == 0:
                    answer = max(answer, 1)
                elif col:
                    map[row_idx][col_idx] = min(map[row_idx][col_idx-1],map[row_idx-1][col_idx],map[row_idx-1][col_idx-1])+1
                    answer = max(answer, map[row_idx][col_idx])
    return answer ** 2