import math
def solution(a, b):
    answer = 0

    while True:
        gcd = 1
        for i in range(2, a + 1):
            if a % i == 0 and b % i == 0:
                gcd = i
        if gcd == 1:
            break
        else:
            a = a // gcd
            b = b // gcd
    while True:
        if b % 2 == 0:
            b = b // 2
        elif b % 5 == 0:
            b = b // 5
        else:
            break

    return 1 if b == 1 else 2