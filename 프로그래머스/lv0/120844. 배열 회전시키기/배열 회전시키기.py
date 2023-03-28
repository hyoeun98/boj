from collections import deque
def solution(numbers, direction):
    queue = deque(numbers)
    if direction == "right":
        queue.rotate(1)
    else:
        queue.rotate(-1)
    return list(queue)