def solution(n, k):
    free_drink = n // 10
    return n * 12000 + (k - free_drink) * 2000