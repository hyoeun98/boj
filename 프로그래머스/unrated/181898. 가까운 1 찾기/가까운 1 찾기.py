def solution(arr, idx):
    for i, v in enumerate(arr[idx:]):
        if v == 1:
            return i + idx
    return -1