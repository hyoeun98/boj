from collections import deque
def solution(food):
    answer = deque('0')
    q = deque()
    for i, v in enumerate(food):
        if v // 2 >= 1:
            q.appendleft([str(i), v//2])
            
    for i in q:
        answer.append(i[0] * i[1])
        answer.appendleft(i[0] * i[1])

    return "".join(answer)