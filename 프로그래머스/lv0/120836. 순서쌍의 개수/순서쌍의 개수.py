def solution(n):
    answer = 0
    for i in range(1, int(n ** 0.5)+1):
        print(i)
        if n % i ==0:
            answer += 2
            if i **2 == n:
                answer -= 1
    return answer