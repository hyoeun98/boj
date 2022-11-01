from collections import deque
def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    rm_blocks = set()
    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != "0":
                    rm_blocks.update([(i,j), (i+1, j), (i, j+1), (i+1,j+1)])
        if not rm_blocks:
            break
        for row, col in rm_blocks:
            board[row][col] = "0"
        answer += len(rm_blocks)
        temp_board = list(map(list, zip(*board)))
        for i, _ in enumerate(temp_board):
            pad_cnt = temp_board[i].count("0")
            que = deque([j for j in temp_board[i] if j != "0"])
            for _ in range(pad_cnt):
                que.appendleft("0")
            temp_board[i] = que
        board = list(map(list, zip(*temp_board)))
        rm_blocks.clear()
    return answer