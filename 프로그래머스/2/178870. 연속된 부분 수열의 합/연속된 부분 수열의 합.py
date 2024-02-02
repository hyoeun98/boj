def solution(sequence, k):
    end = 0
    arr = []
    partial_sum = 0
    
    for start in range(len(sequence)):
        while partial_sum < k and end < len(sequence):
            partial_sum += sequence[end]
            end += 1
        if partial_sum == k:
            arr.append((start, end - 1, end - start))
        partial_sum -= sequence[start]
    arr.sort(key = lambda x: x[2])
            
    return arr[0][:2]