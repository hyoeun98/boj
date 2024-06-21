import sys
import bisect
from collections import deque
n = int(sys.stdin.readline())
board = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    
    board.append(row)
    
sorted_list = deque(sorted(board[-1]))
answer = sorted_list.popleft()
for i in board[:-1]:
    for j in i:
        if j > answer:
            bisect.insort_right(sorted_list, j)
            answer = sorted_list.popleft()
    
print(answer)