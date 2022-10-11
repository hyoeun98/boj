def solution(brown, yellow):
    candidate_list = [(i, yellow // i) for i in range(1, yellow // 2 + 2) if yellow % i == 0]
    for i in candidate_list:
        if i[0] * 2 + i[1] * 2 + 4 == brown:
            return [max(i[0], i[1]) + 2, min(i[0], i[1]) + 2]
