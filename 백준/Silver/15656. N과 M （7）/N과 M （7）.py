import sys

def solution():
    if len(arr) == m:
        print(*arr)
        return
    for i in candidate:
        arr.append(i)
        solution()
        arr.pop()
n, m = map(int, sys.stdin.readline().split())
candidate = list(map(int, sys.stdin.readline().split()))
candidate.sort()
arr = []
solution()