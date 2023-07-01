def solution(dots):
    w, h = 0, 0
    x, y = dots[0]
    for i in dots[1:]:
        if i[0] != x:
            w = max(i[0], x) - min(i[0], x)
        if i[1] != y:
            h = max(i[1], y) - min(i[1], y)
    
    return abs(w) * abs(h)