def solution(emergency):
    answer = []
    emer_list = [[i, v] for i, v in enumerate(emergency)]
    emer_list.sort(key = lambda x: x[1], reverse=True)
    for i, v in enumerate(emer_list):
        v.append(i+1)
    emer_list.sort(key = lambda x:x[0])
    return [i[2] for i in emer_list]