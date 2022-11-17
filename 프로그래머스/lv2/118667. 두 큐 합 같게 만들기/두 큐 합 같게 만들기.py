from collections import deque
def solution(queue1, queue2):
    answer = 0

    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    for _ in range(len(q1) * 4):
        if sum_q1 > sum_q2:
            pop = q1.popleft()
            sum_q2 += pop
            sum_q1 -= pop
            q2.append(pop)
        elif sum_q1 < sum_q2:
            pop = q2.popleft()
            sum_q1 += pop
            sum_q2 -= pop
            q1.append(pop)
        else:
            break
            
        answer += 1
    
    return answer if sum_q1 == sum_q2 else -1