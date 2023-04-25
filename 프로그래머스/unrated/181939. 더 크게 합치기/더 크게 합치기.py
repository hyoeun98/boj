def solution(a, b):
    if (concat_1 := str(a) + str(b)) >= (concat_2 := str(b) + str(a)):
        return int(concat_1)
    else:
        return int(concat_2)
