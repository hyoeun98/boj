def solution(n):
    answer = 0
    for i in range(1, n + 1):
        seq = 0
        for j in range(i, n + 1):
            seq += j
            if seq > n:
                break
            elif seq == n:
                answer += 1
    return answer