def solution(n):
    answer = []
    for i in range(2, n // 2 + 1):
        flag = False
        while n % i == 0:
            n //= i
            flag = True
        if flag:
            answer.append(i)
    
    return answer if answer else [n]