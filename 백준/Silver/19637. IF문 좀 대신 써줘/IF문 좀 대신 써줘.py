import sys
import bisect
def solution():
    n, m = map(int, sys.stdin.readline().split())
    title, limits = [], []
    for _ in range(n):
        name, limit = sys.stdin.readline().split()
        title.append(name)
        limits.append(int(limit))

    for _ in range(m):
        character = int(sys.stdin.readline())
        idx = bisect.bisect_left(limits, character)
        print(title[idx])
solution()
        