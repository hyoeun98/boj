def solution(n):
    n = list(map(int, str(n)))
    sum = 0
    for i in n:
        sum += i
    return sum