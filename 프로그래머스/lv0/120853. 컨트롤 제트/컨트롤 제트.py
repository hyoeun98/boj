def solution(s):
    s = s.split()
    answer = sum(map(lambda x: 0 if x == "Z" else int(x), s))
    for i, v in enumerate(s):
        if v == 'Z':
            answer -= int(s[i-1])
        
    return answer