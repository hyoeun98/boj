def solution(arr, intervals):
    answer = []
    for i in intervals:
        start = i[0]
        end = i[1]+1
        answer.extend(arr[start : end])
    return answer