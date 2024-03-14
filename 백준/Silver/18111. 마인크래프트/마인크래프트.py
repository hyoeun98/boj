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
board.sort(reverse = True)
for i in range(max_depth, min_depth - 1, -1):
    block = b
    time = 0
    invalid = False
    for j in board:
        if j > i:
            block += j - i
            time += (j - i) * 2
        elif j < i:
            if block >= i - j:
                block -= i - j
                time += i - j
            else:
                invalid = True
                break
        else:
            continue
    
    if not invalid:
        if answer[0] > time:
            answer = [time, i]
                    
print(*answer)