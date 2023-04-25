def solution(my_string):
    answer = [my_string[-i:] for i in range(1, len(my_string)+1)]
    answer.sort()
    return answer