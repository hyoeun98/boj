import string
def solution(my_string):
    answer = dict()
    for i in string.ascii_uppercase:
        answer[i] = 0
    for i in string.ascii_lowercase:
        answer[i] = 0
    
    for i in my_string:
        answer[i] += 1
    return list(answer.values())