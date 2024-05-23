import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) < m:
        continue
    arr.append(word)

cnt = Counter(arr)
answer = []
for i in cnt:
    answer.append((i, len(i), cnt[i]))

answer.sort(key = lambda x: (-x[2], -x[1], x[0]))
for i in answer:
    print(i[0])
    