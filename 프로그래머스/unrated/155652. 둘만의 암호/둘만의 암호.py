def solution(s, skip, index):
    answer = []
    skip_list = list(map(ord, skip))
    for i in s:
        temp = ord(i)
        temp_index = index
        while temp_index:
            temp = temp+1 if temp < 122 else 97
            while temp in skip_list:
                temp = temp+1 if temp < 122 else 97
            temp_index -= 1
        answer.append(chr(temp))
    
    return "".join(answer)