def solution(wallpaper):
    arr_i, arr_j = [], []
    for i, line in enumerate(wallpaper):
        for j, code in enumerate(line):
            if code == "#":
                arr_i.append(i)
                arr_j.append(j)
    
    x1, y1, x2, y2 = min(arr_i), min(arr_j), max(arr_i) + 1, max(arr_j) + 1
    return [x1, y1, x2, y2]