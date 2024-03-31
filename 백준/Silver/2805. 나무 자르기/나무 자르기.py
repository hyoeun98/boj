import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(arr)
mid = (start + end) // 2
while start <= end:
    temp = sum([max(0, i - mid) for i in arr])
    if temp < m:
        end = mid - 1
        mid = (start + end) // 2
    elif temp > m:
        start = mid + 1
        mid = (start + end) // 2
    else:
        break
    
    
print(mid)