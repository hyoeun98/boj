def solution(rank, attendance):
    answer = []
    rank = [(v, i) for i, v in enumerate(rank)]
    rank.sort()
    for i in rank:
        if attendance[i[1]]:
            answer.append(i[1])
            if len(answer) >= 3:
                break
    
    return answer[0] * 10000 + answer[1] * 100 + answer[2]