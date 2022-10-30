from collections import deque
def solution(prices):
    answer = []
    stack = deque(prices)
    while stack:
        a = stack.popleft()
        search = False
        for i, v in enumerate(stack):
            if v < a:
                answer.append(i+1)
                search = True
                break
                
            else:
                pass
            
        if not search:
            answer.append(len(stack))
    return answer