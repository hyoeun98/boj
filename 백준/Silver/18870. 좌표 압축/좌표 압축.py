import sys

n = int(sys.stdin.readline())
arr = list(zip(map(int, sys.stdin.readline().split()), range(n + 1)))
answer = [0 for _ in range(n)]
arr.sort()
cnt = 0
for i in range(1, n):
    if arr[i][0] == arr[i - 1][0]:
        answer[arr[i][1]] = answer[arr[i - 1][1]]
        cnt += 1
    else:
        answer[arr[i][1]] = i - cnt
        
print(*answer)

