def solution(elements):
    answer = set()
    for c in range(len(elements)):
        start_idx, end_idx = 0, 1 + c
        circle = elements + elements[:c]
        for i in range(len(elements)):
            answer.add(sum(circle[start_idx:end_idx]))
            start_idx += 1
            end_idx += 1
    return len(answer)