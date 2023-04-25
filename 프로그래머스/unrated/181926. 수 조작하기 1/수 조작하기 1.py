def solution(n, control):
    cntl_dict = {"w" : 1, "s" : -1, "d" : 10, "a" : -10 }
    for i in control:
        n += cntl_dict[i]
    return n