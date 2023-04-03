from collections import Counter
def solution(s):
    answer = []
    cnt = Counter(s)
    for k, v in cnt.items():
        if v == 1:
            answer.append(k)
    answer.sort()
    return "".join(answer)