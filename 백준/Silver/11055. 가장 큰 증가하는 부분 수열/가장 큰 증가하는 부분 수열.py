import sys

def solution():
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [0 for _ in range(n)]
    dp = arr[:]
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + arr[i])

    print(max(dp))
n = int(sys.stdin.readline())
solution()