def solution(s):
    answer = []
    for i, v in enumerate(s):
        idx = s[:i][::-1].find(v)
        answer.append(idx if idx < 0 else idx + 1)
    return answer