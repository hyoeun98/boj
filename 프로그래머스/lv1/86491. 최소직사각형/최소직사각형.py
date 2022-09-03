def solution(sizes):
    new_sizes = [i[:] if i[0] >= i[1] else i[::-1] for i in sizes]
    w = max([i[0] for i in new_sizes])
    h = max([i[1] for i in new_sizes])
    print(w, h)
    
    answer = w * h
    return answer