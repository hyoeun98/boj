import sys
import pprint
ppr = pprint.pprint

def add_adjacent(adjacent, point, student, N):
    y, x = point
    d = [(0 ,1), (0, -1), (1, 0), (-1, 0)]
    for i in d:
        dy, dx = y + i[0], x + i[1]
        if  0 < dy < N + 1 and 0 < dx < N + 1: 
            adjacent[dy][dx].append(student)

def search_adjacent(board, adjacent, wanted, N):
    wanted_stduent_num = 0
    seat = []
    for i in range(1, N + 1):
        for j in range(1,N + 1):
            if board[i][j] != 0:
                continue
            temp = 0
            for k in wanted:
                if k in adjacent[i][j]:
                    temp += 1
            if temp > wanted_stduent_num:
                seat.clear()
                seat.append([i, j])
            elif temp == wanted_stduent_num:
                seat.append([i, j])

            wanted_stduent_num = max(temp, wanted_stduent_num)
    # print(seat, 123)
    seat.sort(key = lambda x: (-([board[x[0] + 1][x[1]], board[x[0] - 1][x[1]], board[x[0]][x[1] + 1], board[x[0]][x[1] - 1]].count(0)), x[1], x[0]))
    # print(seat, 456)
    return seat[0]

def solution():
    N = int(sys.stdin.readline())
    student_dict = dict()
    board = [[1000 for _ in range(N + 2)] for _ in range(N + 2)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            board[i][j] = 0
    adjacent = [[[] for _ in range(N + 2)] for _ in range(N + 2)]

    for _ in range(N **2):
        k, *v = map(int, sys.stdin.readline().split())
        student_dict[k] = v
    
    first_student = list(student_dict.keys())[0]
    board[2][2] = first_student
    add_adjacent(adjacent, (2, 2), first_student, N)
    for i in list(student_dict.keys())[1:]:
        # ppr(adjacent)
        # ppr(board)
        wanted = student_dict[i]
        seat = search_adjacent(board, adjacent, wanted, N)
        board[seat[0]][seat[1]] = i
        add_adjacent(adjacent, seat, i, N)
    answer = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            wanted = student_dict[board[i][j]]
            adj = adjacent[i][j]
            score = 0
            for k in wanted:
                if k in adj:
                    score += 1
            answer += int(10 ** (score - 1))
    #         print(score)
    # ppr(adjacent)
    # ppr(board)

    print(answer)
solution()