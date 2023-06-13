import sys
# 0 북쪽
# 1 동쪽
# 2 남쪽
# 3 서쪽
def cleaning(room, x, y, d):
    cnt = 0
    while True:
        if room[y][x] == 0: # 현재 칸이 청소되지 않은 경우
            room[y][x] = 2
            cnt += 1
            
        elif (x == 0 or room[y][x - 1] != 0) and (x >= M - 1 or room[y][x + 1] != 0) and (y == 0 or room[y - 1][x] != 0) and (y >= N - 1 or room[y + 1][x] != 0): # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
            if d == 0 and y < N - 1 and room[y + 1][x] != 1:
                y += 1
            elif d == 1 and x > 0 and room[y][x -1] != 1:
                x -= 1
            elif d == 2 and y > 0 and room[y - 1][x] != 1:
                y -= 1
            elif d == 3 and x < M - 1 and room[y][x + 1] != 1:
                x += 1
            else:
                break
        
        else: # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
            for _ in range(4): 
                d = 3 if d == 0 else d - 1
                if d == 0 and y > 0 and room[y - 1][x] == 0:
                    y -= 1
                    break
                
                elif d == 1 and x < M + 1 and room[y][x + 1] == 0:
                    x += 1
                    break
                
                elif d == 2 and y < N - 1 and room[y + 1][x] == 0:
                    y += 1
                    break
                
                elif d == 3 and x > 0 and room[y][x - 1] == 0:
                    x -= 1
                    break
    
    print(cnt)
            
        
            
N, M = map(int, sys.stdin.readline().split())
y, x, d = map(int, sys.stdin.readline().split())
room = []
for i in range(N):
    room.append(list(map(int, sys.stdin.readline().split())))
    
# print(room)
cleaning(room, x, y, d)
# print(room)