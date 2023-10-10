import sys

def solution():
    distance = 0
    big, small = max(x, y), min(x, y)
    if 2 * w > s:
        distance += small * s
    else:
        distance += small * (2 * w)

    if (big - small) % 2 == 0:
        distance += min(w, s) * (big - small)
    else:
        distance += min(w, s) * (big - small - 1)
        distance += w

    print(distance)
    
    
    
x, y, w, s = map(int, sys.stdin.readline().split())
solution()
