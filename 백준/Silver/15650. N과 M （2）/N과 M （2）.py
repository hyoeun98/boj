import sys
def back_tracking(start):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(start, n + 1):
        if i not in arr:
            arr.append(i)
            back_tracking(i + 1)
            arr.pop()

def solution():
    back_tracking(1)
    
n, m = map(int, sys.stdin.readline().split())
arr = []
solution()