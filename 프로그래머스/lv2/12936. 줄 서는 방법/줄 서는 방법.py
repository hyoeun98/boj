import math
def solution(n, k):
    answer = []
    candidate = list(range(1, n+1))
    k -= 1

    for i in range(1, n+1):
        answer.append(candidate.pop(k // math.factorial(n-i)))
        k %= math.factorial(n-i)

    return answer