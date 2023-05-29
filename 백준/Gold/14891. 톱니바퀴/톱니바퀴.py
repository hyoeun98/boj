import sys
from collections import deque

def turning(turning_gear, direction):
    gear_1 = None, gear[0][2]
    gear_2 = gear[1][6], gear[1][2]
    gear_3 = gear[2][6], gear[2][2]
    gear_4 = gear[3][6], None
    
    if turning_gear == 1:
        turn_1 = True
        turn_2 = gear_1[1] != gear_2[0] and turn_1
        turn_3 = gear_2[1] != gear_3[0] and turn_2
        turn_4 = gear_3[1] != gear_4[0] and turn_3
        turn_flag = [turn_1, turn_2, turn_3, turn_4]
        
        rotation(gear[0], direction, turn_flag[0])
        rotation(gear[1], -direction, turn_flag[1])
        rotation(gear[2], direction, turn_flag[2])
        rotation(gear[3], -direction, turn_flag[3])

    elif turning_gear == 2:
        turn_2 = True
        turn_1 = gear_2[0] != gear_1[1] and turn_2
        turn_3 = gear_2[1] != gear_3[0] and turn_2
        turn_4 = gear_3[1] != gear_4[0] and turn_3
        turn_flag = [turn_1, turn_2, turn_3, turn_4]
        
        rotation(gear[1], direction, turn_flag[1])
        rotation(gear[0], -direction, turn_flag[0])
        rotation(gear[2], -direction, turn_flag[2])
        rotation(gear[3], direction, turn_flag[3])
        
    elif turning_gear == 3:
        turn_3 = True
        turn_2 = gear_3[0] != gear_2[1] and turn_3
        turn_1 = gear_2[0] != gear_1[1] and turn_2
        turn_4 = gear_3[1] != gear_4[0] and turn_3
        turn_flag = [turn_1, turn_2, turn_3, turn_4]
        
        rotation(gear[2], direction, turn_flag[2])
        rotation(gear[1], -direction, turn_flag[1])
        rotation(gear[3], -direction, turn_flag[3])
        rotation(gear[0], direction, turn_flag[0])
        
    else:
        turn_4 = True
        turn_3 = gear_3[1] != gear_4[0] and turn_4
        turn_2 = gear_2[1] != gear_3[0] and turn_3
        turn_1 = gear_1[1] != gear_2[0] and turn_2
        turn_flag = [turn_1, turn_2, turn_3, turn_4]
        
        rotation(gear[3], direction, turn_flag[3])
        rotation(gear[2], -direction, turn_flag[2])
        rotation(gear[1], direction, turn_flag[1])
        rotation(gear[0], -direction, turn_flag[0])
        
def rotation(rotate_gear, direction, is_turn):
    if is_turn:
        rotate_gear.rotate(direction)
            
gear = []
for _ in range(4):
    gear.append(deque(sys.stdin.readline().strip()))
K = int(sys.stdin.readline())
turn = []
for _ in range(K):
    turn.append(list(map(int, sys.stdin.readline().split())))
    
for i in turn:
    turning(*i)

answer = 0
for i, v in enumerate(gear):
    answer += int(v[0]) * (2 ** i)

print(answer)
