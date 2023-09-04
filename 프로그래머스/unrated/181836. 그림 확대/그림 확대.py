def solution(picture, k):
    answer = []
    for i in picture:
        t = []
        for j in i:
            t.append(j *k)
        for _ in range(k):
            answer.append("".join(t))
    return answer
