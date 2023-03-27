def solution(dot):
    x = dot[0]
    y = dot[1]
    
    if x * y > 0:
        if x > 0:
            return 1
        else:
            return 3
    else:
        if x < 0:
            return 2
        else:
            return 4
        