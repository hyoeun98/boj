def solution(arr, query):
    answer = []
    for i, v in enumerate(query):
        if i % 2 == 0:
            arr = arr[:v + 1]
        else:
            arr = arr[v:]
    return arr