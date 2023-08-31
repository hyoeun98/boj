def solution(chicken):
    answer = 0
    coupon = 0
    while 1:
        coupon += chicken
        if coupon < 10:
            break
        else:
            div, mod = divmod(coupon, 10)
            coupon = mod
            chicken = div
            answer += div
    return answer