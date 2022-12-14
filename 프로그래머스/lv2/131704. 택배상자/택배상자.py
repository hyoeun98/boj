from collections import deque
def solution(order):
    answer = len(order)
    order = deque(order)
    stack = deque()
    queue = deque([i for i in range(1, len(order) + 1)])
    
    while queue:
        box = queue.popleft()
        if box == order[0]:
            del order[0]
        else:
            if not stack:
                stack.append(box)
            else:
                stack_box = stack.pop()
                if stack_box == order[0]:
                    del order[0]
                    queue.appendleft(box)
                else:
                    stack.append(stack_box)
                    stack.append(box)
    
    while stack and stack[-1] == order[0]:
        del stack[-1]
        del order[0]

    return answer - len(order)