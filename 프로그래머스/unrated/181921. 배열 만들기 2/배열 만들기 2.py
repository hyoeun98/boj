def solution(l, r):
    answer = []
    for i in range(l, r+1):
        flag = True
        for j in str(i):
            if j not in ["0", "5"]:
                flag = False
                break
        if flag:
            answer.append(i)
    return answer if answer else [-1]