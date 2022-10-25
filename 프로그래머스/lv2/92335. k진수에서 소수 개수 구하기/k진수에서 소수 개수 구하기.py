import re
def solution(n, k):
    answer = 0
    k_nary_num = ""
    while n:
        n, t = divmod(n, k)
        k_nary_num += str(t)
    k_nary_num = "".join(reversed(k_nary_num))
    k_nary_num = list(map(int, [i for i in k_nary_num.split("0") if i != "" and i != "1"]))
    is_Prime = True
    for i in k_nary_num:
        for j in range(2, int(i ** (1/2)) + 1):
            if i % j == 0:
                is_Prime = False
                break
        answer += 1 if is_Prime else 0
        is_Prime = True
    return answer