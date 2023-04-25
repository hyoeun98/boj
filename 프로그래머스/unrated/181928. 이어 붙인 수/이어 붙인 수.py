def solution(num_list):
    odd = ""
    even = ""
    for i, v in enumerate(num_list):
        if v % 2 == 0:
            even += str(v)
        else:
            odd += str(v)
    
    return int(odd) + int(even)