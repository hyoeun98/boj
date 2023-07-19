import sys
import pprint
import itertools as it
ppr = pprint.pprint

def push_right(board, blue, red):
    blue_y, blue_x = blue
    red_y, red_x, = red
    if blue_y == red_y: # B, R가 같은 row
        if blue_x > red_x:
            while board[blue_y][blue_x + 1] == ".":
                board[blue_y][blue_x + 1], board[blue_y][blue_x] = board[blue_y][blue_x], board[blue_y][blue_x + 1]
                blue_x += 1
            if board[blue_y][blue_x + 1] == "O":
                board[blue_y][blue_x] = "."
                blue_x += 1
            
            while board[red_y][red_x + 1] == ".":
                board[red_y][red_x + 1], board[red_y][red_x] = board[red_y][red_x], board[red_y][red_x + 1]
                red_x += 1
            if board[red_y][red_x + 1] == "O":
                board[red_y][red_x] = "."
                red_x += 1
        else:
            while board[red_y][red_x + 1] == ".":
                board[red_y][red_x + 1], board[red_y][red_x] = board[red_y][red_x], board[red_y][red_x + 1]
                red_x += 1
            if board[red_y][red_x + 1] == "O":
                board[red_y][red_x] = "."
                red_x += 1

            while board[blue_y][blue_x + 1] == ".":
                board[blue_y][blue_x + 1], board[blue_y][blue_x] = board[blue_y][blue_x], board[blue_y][blue_x + 1]
                blue_x += 1
            if board[blue_y][blue_x + 1] == "O":
                board[blue_y][blue_x] = "."
                blue_x += 1

    else: # B, R가 다른 row
        while board[red_y][red_x + 1] == ".":
            board[red_y][red_x + 1], board[red_y][red_x] = board[red_y][red_x], board[red_y][red_x + 1]
            red_x += 1
        if board[red_y][red_x + 1] == "O":
            board[red_y][red_x] = "."
            red_x += 1

        while board[blue_y][blue_x + 1] == ".":
            board[blue_y][blue_x + 1], board[blue_y][blue_x] = board[blue_y][blue_x], board[blue_y][blue_x + 1]
            blue_x += 1
        if board[blue_y][blue_x + 1] == "O":
            board[blue_y][blue_x] = "."
            blue_x += 1
    
    return [blue_y, blue_x], [red_y, red_x]

def push_left(board, blue, red):
    blue_y, blue_x = blue
    red_y, red_x, = red
    if blue_y == red_y: # B, R가 같은 row
        if blue_x < red_x:
            while board[blue_y][blue_x - 1] == ".":
                board[blue_y][blue_x - 1], board[blue_y][blue_x] = board[blue_y][blue_x], board[blue_y][blue_x - 1]
                blue_x -= 1
            if board[blue_y][blue_x - 1] == "O":
                board[blue_y][blue_x] = "."
                blue_x -= 1
            
            while board[red_y][red_x - 1] == ".":
                board[red_y][red_x - 1], board[red_y][red_x] = board[red_y][red_x], board[red_y][red_x - 1]
                red_x -= 1
            if board[red_y][red_x - 1] == "O":
                board[red_y][red_x] = "."
                red_x -= 1
        
        else:
            while board[red_y][red_x - 1] == ".":
                board[red_y][red_x - 1], board[red_y][red_x] = board[red_y][red_x], board[red_y][red_x - 1]
                red_x -= 1
            if board[red_y][red_x - 1] == "O":
                board[red_y][red_x] = "."
                red_x -= 1

            while board[blue_y][blue_x - 1] == ".":
                board[blue_y][blue_x - 1], board[blue_y][blue_x] = board[blue_y][blue_x], board[blue_y][blue_x - 1]
                blue_x -= 1
            if board[blue_y][blue_x - 1] == "O":
                board[blue_y][blue_x] = "."
                blue_x -= 1

    else: # B, R가 다른 row
        while board[red_y][red_x - 1] == ".":
            board[red_y][red_x - 1], board[red_y][red_x] = board[red_y][red_x], board[red_y][red_x - 1]
            red_x -= 1
        if board[red_y][red_x - 1] == "O":
            board[red_y][red_x] = "."
            red_x -= 1

        while board[blue_y][blue_x - 1] == ".":
            board[blue_y][blue_x - 1], board[blue_y][blue_x] = board[blue_y][blue_x], board[blue_y][blue_x - 1]
            blue_x -= 1
        if board[blue_y][blue_x - 1] == "O":
            board[blue_y][blue_x] = "."
            blue_x -= 1

    return [blue_y, blue_x], [red_y, red_x]

def push_up(board, blue, red):
    blue_y, blue_x = blue
    red_y, red_x, = red
    if blue_x == red_x: # B, R가 같은 col
        if blue_y < red_y:
            while board[blue_y - 1][blue_x] == ".":
                board[blue_y- 1][blue_x], board[blue_y][blue_x] = board[blue_y][blue_x], board[blue_y - 1][blue_x]
                blue_y -= 1
            if board[blue_y - 1][blue_x] == "O":
                board[blue_y][blue_x] = "."
                blue_y -= 1

            while board[red_y - 1][red_x] == ".":
                board[red_y - 1][red_x], board[red_y][red_x] = board[red_y][red_x], board[red_y - 1][red_x]
                red_y -= 1
            if board[red_y - 1][red_x] == "O":
                board[red_y][red_x] = "."
                red_y -= 1
        else:
            while board[red_y - 1][red_x] == ".":
                board[red_y - 1][red_x], board[red_y][red_x] = board[red_y][red_x], board[red_y - 1][red_x]
                red_y -= 1
            if board[red_y - 1][red_x] == "O":
                board[red_y][red_x] = "."
                red_y -= 1

            while board[blue_y - 1][blue_x] == ".":
                board[blue_y- 1][blue_x], board[blue_y][blue_x] = board[blue_y][blue_x], board[blue_y - 1][blue_x]
                blue_y -= 1
            if board[blue_y - 1][blue_x] == "O":
                board[blue_y][blue_x] = "."
                blue_y -= 1
    
    else: # B, R가 다른 col
        while board[red_y - 1][red_x] == ".":
            board[red_y - 1][red_x], board[red_y][red_x] = board[red_y][red_x], board[red_y - 1][red_x]
            red_y -= 1
        if board[red_y - 1][red_x] == "O":
            board[red_y][red_x] = "."
            red_y -= 1

        while board[blue_y - 1][blue_x] == ".":
            board[blue_y- 1][blue_x], board[blue_y][blue_x] = board[blue_y][blue_x], board[blue_y - 1][blue_x]
            blue_y -= 1
        if board[blue_y - 1][blue_x] == "O":
            board[blue_y][blue_x] = "."
            blue_y -= 1

    return [blue_y, blue_x], [red_y, red_x]

def push_down(board, blue, red):
    blue_y, blue_x = blue
    red_y, red_x, = red
    if blue_x == red_x: # B, R가 같은 col
        if blue_y > red_y:
            while board[blue_y + 1][blue_x] == ".":
                board[blue_y + 1][blue_x], board[blue_y][blue_x] = board[blue_y][blue_x], board[blue_y + 1][blue_x]
                blue_y += 1
            if board[blue_y + 1][blue_x] == "O":
                board[red_y][red_x] = "."
                blue_y += 1
                
            
            while board[red_y + 1][red_x] == ".":
                board[red_y + 1][red_x], board[red_y][red_x] = board[red_y][red_x], board[red_y + 1][red_x]
                red_y += 1
            if board[red_y + 1][red_x] == "O":
                board[red_y][red_x] = "."
                red_y += 1
        else:
            while board[red_y + 1][red_x] == ".":
                board[red_y + 1][red_x], board[red_y][red_x] = board[red_y][red_x], board[red_y + 1][red_x]
                red_y += 1
            if board[red_y + 1][red_x] == "O":
                board[red_y][red_x] = "."
                red_y += 1

            while board[blue_y + 1][blue_x] == ".":
                board[blue_y + 1][blue_x], board[blue_y][blue_x] = board[blue_y][blue_x], board[blue_y + 1][blue_x]
                blue_y += 1
            if board[blue_y + 1][blue_x] == "O":
                board[red_y][red_x] = "."
                blue_y += 1

    else: # B, R가 다른 col
        while board[red_y + 1][red_x] == ".":
            board[red_y + 1][red_x], board[red_y][red_x] = board[red_y][red_x], board[red_y + 1][red_x]
            red_y += 1
        if board[red_y + 1][red_x] == "O":
            board[red_y][red_x] = "."
            red_y += 1

        while board[blue_y + 1][blue_x] == ".":
            board[blue_y + 1][blue_x], board[blue_y][blue_x] = board[blue_y][blue_x], board[blue_y + 1][blue_x]
            blue_y += 1
        if board[blue_y + 1][blue_x] == "O":
            board[red_y][red_x] = "."
            blue_y += 1

    return [blue_y, blue_x], [red_y, red_x]

def solution():
    N, M = map(int, sys.stdin.readline().split())
    board_original = []
    for _ in range(N):
        board_original.append(list(sys.stdin.readline().strip()))
    
    for i, line in enumerate(board_original):
        for j, v in enumerate(line):
            if v == "R":
                red_original = [i, j]
            elif v == "B":
                blue_original = [i, j]
            elif v == "O":
                hole = [i, j]
    
    # print(red_original, blue_original)
    # ppr(board_original)
    answer = 100
    pushes = [push_right, push_left, push_up, push_down]

    push_pd = it.product(pushes, repeat = 10)
    def has_continuous_duplicates(lst):
        return not any( x == y for x, y in zip(lst, lst[1:]))

    # 연속으로 중복된 값이 없는 순열 필터링
    filtered_pushes = [perm for perm in push_pd if has_continuous_duplicates(perm)]

    for push in filtered_pushes:
        board = [b[:] for b in board_original]
        blue = blue_original[:]
        red = red_original[:]
        # print("________________")
        for i, p in enumerate(push):
            if i+1 >= answer:
                break
            # print(p.__name__)
            blue, red = p(board, blue, red)
            
            # print(red,blue)
            if blue[0] == hole[0] and blue[1] == hole[1]:
                break
            elif red[0] == hole[0] and red[1] == hole[1]:
                answer = min(answer, i+1)
                
                break
                    
    # ppr(board_original)
    print(answer if answer != 100 else -1)
solution()