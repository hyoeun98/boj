import sys

n, l = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
center = arr.pop()
cnt = 1
flag = True
for i in reversed(arr):
    if i - l < center / cnt < i + l:
        center += i
        cnt += 1
    else:
        print("unstable")
        flag = False
        break
    
if flag:
    print("stable")