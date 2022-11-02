import itertools as it
def solution(numbers):
    answer = []
    for i in numbers:
        i_bin = bin(i)[2:]
        if i_bin.endswith("0"):
            t = list(i_bin)
            t[-1] = "1"
        else:
            idx = i_bin.rfind("0")
            if idx == -1:
                t = list("0" + i_bin)
                idx = 0
            else:
                t = list(i_bin)
            t[idx] = "1"
            t[idx+1] = "0"
        answer.append(int("".join(t), 2))
    return answer