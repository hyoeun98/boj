def solution(my_string):
    my_list = my_string
    answer = list(dict.fromkeys(my_list))

    return "".join(answer)