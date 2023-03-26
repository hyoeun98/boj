from collections import Counter
def solution(array):
    if len(set(array)) < 2:
        return  array[0]
    
    counter = Counter(array)
    first, second = counter.most_common(2)
    if first[1] == second[1]:
        return -1
    else:
        return first[0]