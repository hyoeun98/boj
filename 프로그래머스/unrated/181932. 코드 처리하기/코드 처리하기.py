def solution(code):
    answer = ''
    mode = 0
    for i, v in enumerate(code):
        if v == '1':
            mode = 0 if mode == 1 else 1
        elif mode == 0 and i % 2 == 0:
            answer += v
        elif mode == 1 and i % 2 == 1:
            answer += v
    return answer if answer else "EMPTY"