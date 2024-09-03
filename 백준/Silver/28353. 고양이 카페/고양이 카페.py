import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort(reverse = True)
answer = 0

while len(arr) >= 2:
    if arr[0] + arr[-1] > k:
        del arr[0]
    else:
        answer += 1
        del arr[0]
        del arr[-1]

print(answer)