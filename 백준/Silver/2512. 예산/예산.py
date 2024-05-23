import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start = 1
end = max(arr)
mid = (start + end) // 2
answer = 1
while start <= end:
    cnt = 0
    for i in arr:
        if mid <= i:
            cnt += mid
        else:
            cnt += i
    if cnt <= m:
         start = mid + 1
         answer = mid
    else:
        end = mid - 1

    mid = (start + end) // 2
    
print(answer)