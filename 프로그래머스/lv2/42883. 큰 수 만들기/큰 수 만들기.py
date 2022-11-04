from collections import deque
def solution(number, k):
    c = deque(number)
    arr = deque(c.popleft())
    
    while c and k:
        t = c.popleft()
        while k and arr and arr[-1] < t:
            arr.pop()
            k -= 1
        arr.append(t) 
        
    arr.extend(c)
    
    if k:
        arr.pop()
        
    return "".join(arr)