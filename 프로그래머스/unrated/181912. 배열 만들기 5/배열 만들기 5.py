def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        if k < (temp := int(i[s:s+l])):
            answer.append(temp)
    return answer