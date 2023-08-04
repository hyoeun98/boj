def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        temp_arr = list(filter(lambda x: x > k,arr[s:e + 1]))
        answer.append(min(temp_arr) if temp_arr else -1)
            
    return answer