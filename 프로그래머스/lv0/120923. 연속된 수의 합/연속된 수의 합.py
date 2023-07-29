def solution(num, total):
    answer = []
    for i in range(-num, total + 1):
        temp = [j for j in range(i, i + num)]
        if sum(temp) == total:
            return temp
            
    return answer