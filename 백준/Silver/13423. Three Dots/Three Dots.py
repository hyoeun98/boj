import sys
import bisect
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr_set = set(arr)
    arr.sort()
    answer = 0
    for i in range(n):
        for j in range(i + 1, n):
            diff = arr[j] - arr[i]
            if (diff + arr[j]) in arr_set:
                answer += 1
                    
    print(answer)
    
