import sys

def solution(start):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(start, n):
        if candidate[i] not in arr:
            arr.append(candidate[i])
            solution(i + 1)
            arr.pop()
n, m = map(int, sys.stdin.readline().split())
candidate = list(map(int, sys.stdin.readline().split()))
candidate.sort()
arr = []
solution(0)