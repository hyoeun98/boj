def solution(my_string, is_suffix):
    len_suffix = len(is_suffix)
    return 1 if my_string[-len_suffix:] == is_suffix else 0