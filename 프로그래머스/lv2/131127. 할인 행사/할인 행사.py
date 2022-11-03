from collections import deque
def solution(want, number, discount):
    answer = 0
    discount = deque(discount)
    want_dict = dict()
    sale_list = deque()
    
    for i, v in enumerate(want):
        want_dict[v] = number[i]
    
    for i in range(10):
        d = discount.popleft()
        sale_list.appendleft(d)
        if d in want_dict.keys():
            want_dict[d] -= 1
            
    if not any([i > 0 for i in want_dict.values()]):
        answer += 1
    
    while discount:
        p = sale_list.pop()
        if p in want_dict:
            want_dict[p] += 1
            
        d = discount.popleft()
        sale_list.appendleft(d)
        if d in want_dict:
            want_dict[d] -= 1
        if not any([i > 0 for i in want_dict.values()]):
            answer += 1
    
    return answer