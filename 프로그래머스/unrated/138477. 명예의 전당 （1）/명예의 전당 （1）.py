def solution(k, score):
    queue, answer = [], []
    for i in score:
        if len(queue) < k:
            queue.append(i)
        elif queue[-1] < i:
            queue[-1] = i
        else:
            pass
        queue.sort(reverse=True)
        answer.append(queue[-1])
    return answer