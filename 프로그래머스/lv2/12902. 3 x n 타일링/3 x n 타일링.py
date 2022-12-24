from collections import deque
def solution(n):
    answer = deque([3, 1])
    for i in range(n // 2 - 1):
        answer.appendleft(4 * answer[0] - answer[1])
    return answer[0] % 1_000_000_007