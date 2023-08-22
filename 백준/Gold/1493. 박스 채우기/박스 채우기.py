import sys

def solution():
    answer = 0
    volume = l * w * h
    current_cube_num = 0
    for s, n in cube:
        edge = 2 ** s # 현재 한 변의 길이
        current_cube_num *= 8 # 큰 cube를 작은 cube로 변환
        temp_num = (l // edge) * (w // edge) * (h  // edge) - current_cube_num # 현재 크기로 채울 수 있는 개수 - 현재까지 채운 개수
        temp_num = min(temp_num, n) # 현재 크기의 cube로 채울 수 있는 최대 개수

        answer += temp_num
        current_cube_num += temp_num

    if current_cube_num == volume: # 총 부피와 cube의 부피가 같으면
        print(answer)
    else:
        print(-1)

    

l, w, h = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
cube = []
for _ in range(n):
    cube.append(list(map(int, sys.stdin.readline().split())))
cube.reverse()

solution()
