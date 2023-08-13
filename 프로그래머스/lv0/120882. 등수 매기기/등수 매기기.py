def solution(score):
    answer = []
    avg = list(map(lambda x: sum(x) / 2, score))
    score = avg[:]
    avg.sort(reverse = True)
    for i in score:
        answer.append(avg.index(i) + 1)
    return answer