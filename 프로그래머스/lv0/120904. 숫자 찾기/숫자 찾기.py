def solution(num, k):
    num = str(num)
    answer = num.find(str(k))
    return answer+1 if answer >= 0 else -1