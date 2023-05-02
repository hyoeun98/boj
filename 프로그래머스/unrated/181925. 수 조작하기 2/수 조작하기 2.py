def solution(numLog):
    answer = ''
    for i, v in enumerate(numLog[:-1]):
        next_log = numLog[i+1]
        if v + 1 == next_log:
            answer += "w"
        elif v - 1 == next_log:
            answer += "s"
        elif v + 10 == next_log:
            answer += "d"
        else:
            answer += "a"
    return answer