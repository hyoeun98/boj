from collections import Counter
def solution(k, tangerine):
    c = Counter(tangerine)
    cnt = 0
    for i in sorted(c.values(), reverse = True):
        k -= i
        cnt += 1
        if k <= 0:
            break
    return cnt