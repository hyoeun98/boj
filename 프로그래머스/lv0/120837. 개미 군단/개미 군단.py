def solution(hp):
    answer = 0
    for i in [5, 3, 1]:
        a, b = divmod(hp, i)
        answer += a
        hp = b
    return answer