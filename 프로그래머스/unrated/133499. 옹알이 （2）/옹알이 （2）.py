import re
def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        match_list = []
        for j in pron:
            match = re.finditer(j, i)
            for k in match:
                match_list.append([k.span(), j])
        match_list.sort()
        start, end = 0, 0
        last_word = ''
        for m in match_list:
            if end == m[0][0] and m[1] != last_word:
                start, end = end, m[0][1]
                last_word = m[1]
            else:
                break
                
        if end == len(i):
            answer += 1
                
    return answer