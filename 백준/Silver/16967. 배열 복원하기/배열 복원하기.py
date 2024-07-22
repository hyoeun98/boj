import sys

h, w, x, y = map(int, sys.stdin.readline().split())
arr = []
for _ in range(h + x):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(x, h):
    for j in range(y, w):
        arr[i][j] = arr[i][j] - arr[i - x][j - y]

for i in range(h):
    for j in range(w):
        print(arr[i][j], end = " ")
    print()