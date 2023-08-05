def solution(keyinput, board):
    answer = []
    x, y = 0, 0
    if board == [1, 1]:
        return [0, 0]
    w_limit = board[0] // 2
    h_limit = board[1] // 2
    dir_dict = {"left" : [-1, 0],
                "right" : [1, 0],
                "down" : [0, -1],
                "up" : [0, 1]}
    for i in keyinput:
        dx, dy = dir_dict[i]
        if (dx == 1 and x == w_limit) or (dx == -1 and -x == w_limit):
            pass
        else:
            x += dx
        
        if (dy == 1 and y == h_limit) or (dy == -1 and -y == h_limit):
            pass
        else:
            y += dy
            
    return [x, y]