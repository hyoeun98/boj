from collections import Counter
def solution(lines):
    arr = []
    for i in lines:
        arr.extend([i for i in range(i[0], i[1])])
    
    cnt = Counter(arr)

    answer = len(list(filter(lambda x: x > 1, cnt.values())))
    
    return answer