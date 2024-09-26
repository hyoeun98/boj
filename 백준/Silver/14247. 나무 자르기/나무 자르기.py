import sys

n = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
answer = 0
cnt = 0
sorted_a = [(v, i) for i, v in enumerate(a)]
sorted_a.sort()
for value, idx in sorted_a:
    answer += cnt * value + h[idx]
    cnt += 1
print(answer)