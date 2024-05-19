import sys
from collections import Counter
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    cnt = Counter(arr)
    for i in cnt:
        if cnt[i] < 6:
            for _ in range(cnt[i]):
                arr.remove(i)
    scores = [[] for _ in range(max(arr) + 1)]
    # print(scores)
    for i, v in enumerate(arr):
        scores[v].append(i + 1)
    
    answer = [sum(i[:4]) if i else 1e9 for i in scores[1:]]
    if answer.count(min(answer)) == 1:
        print(answer.index(min(answer)) + 1)
    else:
        candidate = []
        for i, v in enumerate(answer):
            if v == min(answer):
                candidate.append((scores[i + 1][4], i + 1))
        candidate.sort()
        print(candidate[0][1])
                