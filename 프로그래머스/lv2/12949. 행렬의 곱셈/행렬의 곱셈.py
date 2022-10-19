def solution(arr1, arr2):
    answer = []
    arr2_T = list(zip(*arr2))
    
    for i in arr1:
        row = []
        for j in range(len(arr2_T)):
            row.append(sum(list(map(lambda a, b: a * b, i,arr2_T[j]))))
        answer.append(row)
        
    return answer