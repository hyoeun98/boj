def solution(a, b):
    a_is_odd = True if a % 2 == 1 else False
    b_is_odd = True if b % 2 == 1 else False
    if a_is_odd and b_is_odd:
        return a ** 2 + b ** 2
    elif a_is_odd or b_is_odd:
        return 2 * (a + b)
    else:
        return abs(a - b)