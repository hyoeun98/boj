def solution(n, left, right):
    start = [left // n, left % n]
    offset = max(start) + 1
    answer = []
    for _ in range(right - left + 1):
        answer.append(offset)
        start[1] += 1
        if start[1] > (n - 1):
            start[0] += 1
            start[1] = 0
            
        offset = max(start) + 1
            
    return answer