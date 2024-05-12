import sys

h, w, n, m = map(int, sys.stdin.readline().split())
if h == 0 or w == 0:
    print(0)

else:
    answer = [1, 1]
    row = 1
    col = 1
    while True:
        row += n + 1
        if row > h:
            break
        answer[0] += 1
        
    while True:
        col += m + 1
        if col > w:
            break
        answer[1] += 1
        
    print(answer[0] * answer[1])
