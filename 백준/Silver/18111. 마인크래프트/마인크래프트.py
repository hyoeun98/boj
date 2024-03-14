import sys

n, m, b = map(int, sys.stdin.readline().split())
board = []
max_depth = 0
min_depth = 257
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    max_depth = max(max_depth, max(temp))
    min_depth = min(min_depth, min(temp))
    board.extend(temp)

answer = [1e12 ,0]
for i in range(max_depth, min_depth - 1, -1):
    block = b
    time = 0
    for j in board:
        if j > i:
            block += j - i
            time += (j - i) * 2
        elif j < i:
            block -= i - j
            time += i - j
        else:
            continue
    
    if block >= 0:
        if answer[0] > time:
            answer = [time, i]
                    
print(*answer)