def solution(a, d, included):
    answer = 0
    for i, v in enumerate(included):
        if v:
            answer += a + d * i
    return answer