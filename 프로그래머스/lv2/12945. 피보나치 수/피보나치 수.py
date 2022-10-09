def solution(n):
    fibo_first = 0
    fibo_second = 1
    
    for i in range(n-1):
        tmp = fibo_first + fibo_second
        fibo_first = fibo_second
        fibo_second = tmp
        
    answer = fibo_second % 1234567
    return answer