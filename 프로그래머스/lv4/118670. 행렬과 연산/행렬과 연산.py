from collections import deque

def solution(rc, operations):
    answer = []
    mid, left, right = deque(), deque(), deque()
    for r in rc:
        mid.append(deque(r[1:-1]))
        left.append(r[0])
        right.append(r[-1])
        
    for op in operations:
        if op == "Rotate":
            if mid[0]:
                right.appendleft(mid[0].pop())
                mid[-1].append(right.pop())
            else:
                right.appendleft(left.popleft())
            
            if mid[-1]:
                left.append(mid[-1].popleft())
                mid[0].appendleft(left.popleft())
            else:
                left.append(right.pop())
        
        else: # ShiftRow
            mid.rotate(1)
            left.rotate(1)
            right.rotate(1)
            
    for m ,l ,r in zip(mid, left, right):
        answer.append([l] + list(m) + [r])
    return answer