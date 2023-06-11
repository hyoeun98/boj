def solution(arr, queries):
    answer = []
    for i in queries:
        s, e, k = i
        for idx, j in enumerate(arr):
            if s <= idx <= e and idx % k == 0:
                arr[idx] += 1
                
    return arr