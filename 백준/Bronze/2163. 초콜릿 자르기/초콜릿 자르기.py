import sys

def solution():
    answer = 0
    answer += n - 1
    answer += n * (m - 1)
    print(answer)

n, m = map(int, sys.stdin.readline().split())
solution()