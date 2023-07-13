import sys
from collections import deque

def dust_diffusion(room, C, R):
    dust = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(R):
        for j in range(C):
            if (dust_cost := room[i][j]) >= 5:
                dust.append([i, j, dust_cost])
    
    for i in dust[:]:
        diffused_dust = i[2] // 5
        diffused_cnt = 0
        for j in range(4):
            y = i[0] + dy[j]
            x = i[1] + dx[j]
            
            if 0 <= x < C and 0 <= y < R and room[y][x] >= 0:
                room[y][x] += diffused_dust
                diffused_cnt += 1

        room[i[0]][i[1]] -= diffused_dust * diffused_cnt
    
def cleaning(room, C, R, cleaner):
    temp = room[cleaner[0]][-1]
    for i in range(C-1, 1, -1):
        room[cleaner[0]][i] = room[cleaner[0]][i-1]
    room[cleaner[0]][1] = 0

    for i in range(cleaner[0] - 1, -1, -1):
        room[i][C-1], temp = temp, room[i][C-1]
    
    for i in range(C-2, -1, -1):
        room[0][i], temp = temp, room[0][i]

    for i in range(1, cleaner[0]):
        room[i][0], temp = temp, room[i][0]

    temp = room[cleaner[1]][-1]
    for i in range(C-1, 1, -1):
        room[cleaner[1]][i] = room[cleaner[1]][i-1]
    room[cleaner[1]][1] = 0

    for i in range(cleaner[1] + 1, R):
        room[i][C-1], temp = temp, room[i][C-1]
    
    for i in range(C-2, -1, -1):
        room[R-1][i], temp = temp, room[R-1][i]

    for i in range(R-2, cleaner[1], -1):
        room[i][0], temp = temp, room[i][0]

def solution():
    R, C, T = map(int, sys.stdin.readline().split())
    room = []
    for _ in range(R):
        room.append(list(map(int, sys.stdin.readline().split())))
    for i, _ in enumerate(room):
        if room[i][0] == -1:
            cleaner = [i, i+1]
            break

    for _ in range(T):
        dust_diffusion(room, C, R)
        cleaning(room, C, R, cleaner)
        
    answer = 0
    for i in room:
        answer += sum(i)
    print(answer + 2)
solution()

