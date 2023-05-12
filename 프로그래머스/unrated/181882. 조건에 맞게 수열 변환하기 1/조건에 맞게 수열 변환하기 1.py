def solution(arr):
    for i, v in enumerate(arr):
        if v >= 50 and v % 2 == 0:
            arr[i] = v // 2
        elif v < 50 and v % 2 == 1:
            arr[i] = v * 2
    return arr