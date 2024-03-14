import sys

k, n = map(int, sys.stdin.readline().split())
arr = []
start, end = 1, 0
for _ in range(k):
    arr.append(t := int(sys.stdin.readline()))
    end = max(end, t)


while start <= end:
    
    mid = (start + end) // 2
    cnt = sum(map(lambda x: x // mid, arr))
    
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)