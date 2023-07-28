def solution(n):
    answer = [n]
    while (last := answer[-1]) != 1:
        if last % 2 == 0:
            answer.append(last // 2)
        else:
            answer.append(last * 3 + 1)
    return answer