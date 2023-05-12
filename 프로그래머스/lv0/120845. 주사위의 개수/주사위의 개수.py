def solution(box, n):
    w, h, c = box
    answer = (w // n) * (h // n) * (c // n)
    return answer