import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

sorted_arr = sorted(set(arr))

dict = {v:i for i, v in enumerate(sorted_arr)}
print(*(map(lambda x: dict[x], arr)))