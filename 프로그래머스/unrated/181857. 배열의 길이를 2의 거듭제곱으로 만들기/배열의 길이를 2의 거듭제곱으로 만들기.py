def solution(arr):
    zero_num = len(arr)
    answer = 1
    while answer < zero_num:
        answer *= 2
    t = answer - zero_num
    arr.extend([0 for _ in range(t)])
    return arr