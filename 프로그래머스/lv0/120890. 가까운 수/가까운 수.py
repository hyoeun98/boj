def solution(array, n):
    array.sort()
    diff = list(map(lambda x: abs(n - x), array))
    return array[diff.index(min(diff))]