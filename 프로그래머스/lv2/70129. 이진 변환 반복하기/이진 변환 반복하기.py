def solution(s):
    answer = [0, 0]
    while s != "1":
        num_zero = len(s)
        s = s.replace("0", "")
        num_zero -= len(s)
        s = str((bin(len(s))))[2:]
        answer[0] += 1
        answer[1] += num_zero
    return answer