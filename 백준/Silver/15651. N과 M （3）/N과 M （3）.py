import sys
def back_tracking():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n + 1):
        arr.append(i)
        back_tracking()
        arr.pop()

def solution():
    back_tracking()
    
n, m = map(int, sys.stdin.readline().split())
arr = []
solution()