def solution(arr, n):
    is_odd = True if len(arr) % 2 == 1 else False
    if is_odd:
        arr = [v if i % 2 == 1 else v + n for i, v in enumerate(arr)]
    else:
        arr = [v if i % 2 == 0 else v + n for i, v in enumerate(arr)]
    return arr