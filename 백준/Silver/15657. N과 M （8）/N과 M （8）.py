import sys

def solution(start):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(start, n):
        arr.append(candidate[i])
        solution(i)
        arr.pop()
n, m = map(int, sys.stdin.readline().split())
candidate = list(map(int, sys.stdin.readline().split()))
candidate.sort()
arr = []
solution(0)