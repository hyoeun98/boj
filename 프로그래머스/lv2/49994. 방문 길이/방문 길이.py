def solution(dirs):
    co = [0 ,0]
    dir_dict = {"U" : [0, 1], "D" : [0, -1], "L" : [-1, 0], "R" : [1, 0]}
    path_list = []
    for i in dirs:
        t_co = co[:]
        for j in range(2):
            co[j] += dir_dict[i][j]
            if co[j] < 0:
                co[j] = max(-5, co[j])
            else:
                co[j] = min(5, co[j])
        if t_co == co: 
            continue
            
        path_list.append(tuple(t_co + co))
        path_list.append(tuple(co + t_co))
    return len(set(path_list)) // 2