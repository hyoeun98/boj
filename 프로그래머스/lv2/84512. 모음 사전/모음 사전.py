import itertools as it
def solution(word):
    answer = 0
    dict_string = "AEIOU"
    offset = [5 ** i for i in range(len(dict_string), 0, -1)]
    for i, v in enumerate(word):
        o = sum(offset[i:]) // 5
        answer += dict_string.index(v) * o + 1
    return answer
            
