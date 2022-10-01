import math
def solution(n):
    answer = n - 1 # 1 제외
    for i in range(2, n+1):
        for j in range(2, math.floor(i ** (1/2)) +1):
            if i % j == 0:
                answer -= 1
                break
    return answer