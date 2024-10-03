import sys
import bisect
n = int(sys.stdin.readline())
arr = []
x = []
y = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))
    x.append(a)
    y.append(b)
q = int(sys.stdin.readline())
questions = []
for _ in range(q):
    questions.append(float(sys.stdin.readline()))
    
for i in questions:
    if i == 0:
        print(0)
    else:
        idx = bisect.bisect_right(x, i)
        if y[idx - 1] > y[idx]:
            print(-1)
        elif y[idx - 1] < y[idx]:
            print(1)
        else:
            print(0)