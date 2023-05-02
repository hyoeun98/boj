def solution(numbers, k):
    cycle = numbers * k
    return cycle[(k-1) * 2]