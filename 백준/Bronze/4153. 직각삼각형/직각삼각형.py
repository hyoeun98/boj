import sys

while True:
    lines = list(map(int, sys.stdin.readline().split()))
    if lines[0] == lines[1] == lines[2] == 0:
        break
    lines.sort()
    lines = list(map(lambda x : x ** 2, lines))
    if sum(lines[:2]) == lines[2]:
        print("right")
    else:
        print("wrong")
    
        