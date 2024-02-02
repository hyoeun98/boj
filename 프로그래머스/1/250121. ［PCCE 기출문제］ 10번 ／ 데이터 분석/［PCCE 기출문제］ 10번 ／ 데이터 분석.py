def solution(data, ext, val_ext, sort_by):
    ext_dict = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}
    idx = ext_dict[ext]
    data = [i for i in data if i[idx] < val_ext]
    sort_idx = ext_dict[sort_by]
    data.sort(key = lambda x: x[sort_idx])
    return data