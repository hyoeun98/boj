import sys
def bin_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for i in range(1, N + 1):
            cnt += min(mid // i, N)

        # print("cnt", cnt)
        if cnt >= k:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start, end = 1, k

print(bin_search(start, end))