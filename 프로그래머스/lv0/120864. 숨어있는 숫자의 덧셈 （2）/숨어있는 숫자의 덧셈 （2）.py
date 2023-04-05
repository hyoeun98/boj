import re
def solution(my_string):
    sub_string = re.sub("[a-zA-Z]", " ", my_string)
    return sum(map(int ,sub_string.split()))