from collections import Counter
def solution(a, b, c, d):
    answer = 0
    cnt = Counter([a, b, c, d])
    comm = cnt.most_common()
    uniq = len(cnt)
    if uniq == 1:
        answer += 1111 * a
    elif uniq == 4:
        answer += min(cnt)
    elif uniq == 3:
        q, r = comm[1][0], comm[2][0]
        answer += q * r
    elif uniq == 2:
        if comm[0][1] == 3:
            answer += (10 * comm[0][0] + comm[1][0]) ** 2
        else:
            answer += (comm[0][0] + comm[1][0]) * abs(comm[0][0] - comm[1][0])
        
    return answer