import sys

n, m, k, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
answer = [0 for _ in range(n + 1)]
score = [x for _ in range(n + 1)]
if x < k:
    answer[0] = 1

cnt = 1
for i in arr:
    score[cnt] = score[cnt - 1] + i
    if score[cnt] < k:
        answer[cnt] = 1
    cnt += 1
    
cnt = 1
for i in range(len(answer) - 1):
    answer[cnt] += answer[cnt - 1]
    cnt += 1

for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    print(answer[r - 1] - answer[l - 1])
    
