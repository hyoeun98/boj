import sys

n, k = map(int, sys.stdin.readline().split())
arr = [i for i in range(n + 1)]
arr[1] = 0
current = 2
cnt = 0
while sum(arr) != 0:
    p = arr[current]
    for i in range(p, n + 1, p):
        if arr[i] != 0:
            arr[i] = 0
            cnt += 1
            if cnt == k:
                print(i)
                break    
    if cnt == k:
        break
    
    for i in arr:
        if i != 0:
            current = i
            break 