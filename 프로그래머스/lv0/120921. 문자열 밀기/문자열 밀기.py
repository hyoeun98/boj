from collections import deque
def solution(A, B):
    answer = 0
    if A == B:
        return answer
    A = deque(A)
    B = deque(B)
    
    for _ in range(len(A)):
        A.rotate(1)
        answer += 1
        if A == B:
            return answer 
        
    return -1