def solution(s):
    answer = 0
    num_x = 0
    num_not_x = 0
    x = 0
    for i, v in enumerate(s):
        if x == 0:
            x = s[i]
        if v == x:
            num_x += 1
        else:
            num_not_x += 1
            
        if num_x == num_not_x:
            answer += 1
            num_x = 0
            num_not_x = 0
            x = 0
            
    if num_x != num_not_x:
        answer += 1
        
    return answer