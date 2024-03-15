import sys
from collections import deque
def check(a, b, c, d):
            
    sub_board = set(board[i][j] for i in range(a, c) for j in range(b, d))
    if len(sub_board) == 2:
        return -1
    else:
        return sub_board.pop()
    
n = int(sys.stdin.readline())
board = []
answer = [0, 0]
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

cnt = n ** 2
coor_queue = deque()
coor_queue.append([0, 0, n, n])
while cnt > 0:
    a, b, c, d = coor_queue.popleft()
    if (color := check(a, b, c, d)) == -1:
        coor_queue.append([a, b, (a + c) // 2, (b + d) // 2])
        coor_queue.append([a, (b + d) // 2, (a + c) // 2, d])
        coor_queue.append([(a + c) // 2, b, c, (b + d) // 2])
        coor_queue.append([(a + c) // 2, (b + d) // 2, c, d])
    else:
        cnt -= (c - a) * (d - b)
        answer[color] += 1
        
print(answer[0])
print(answer[1])