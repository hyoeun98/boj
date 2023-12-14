import sys
import re
r, c = map(int, sys.stdin.readline().split())
board = []
for _ in range(r):
    line = sys.stdin.readline().strip()
    if re.search('\d', line):
        line = line[:-1].rstrip(".")
        line = line.lstrip("S")
        board.append((int(line[-1]), line.count(".")))

board.sort(key = lambda x: x[1], reverse = True)
answer = [0 for _ in range(9)]
cnt = 100
rank = 0
for i in board:
    if i[1] < cnt:
        cnt = i[1]
        rank += 1
    answer[i[0] - 1] = rank
for i in answer:
    print(i)