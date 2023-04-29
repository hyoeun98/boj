def solution(my_strings, parts):
    answer = ''
    for i, v in enumerate(parts):
        answer += my_strings[i][v[0] : v[1]+1]
    return answer