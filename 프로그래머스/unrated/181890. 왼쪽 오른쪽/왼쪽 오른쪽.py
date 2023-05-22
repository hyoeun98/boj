def solution(str_list):
    str_list = ''.join(str_list)
    l_index = str_list.find("l")
    r_index = str_list.find("r")
    print(l_index, r_index)
    if r_index == -1 and l_index == -1:
        return []
    elif r_index == -1:
        return list(str_list[:l_index])
    elif l_index == -1:
        return list(str_list[r_index+1:])
    elif l_index < r_index:
        return list(str_list[:l_index])
    elif l_index > r_index:
        return list(str_list[r_index+1:])
