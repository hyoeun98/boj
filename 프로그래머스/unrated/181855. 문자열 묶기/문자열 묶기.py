from collections import defaultdict
def solution(strArr):
    answer = defaultdict(int)
    for i in strArr:
        answer[len(i)] += 1
    return sorted(answer.values())[-1]