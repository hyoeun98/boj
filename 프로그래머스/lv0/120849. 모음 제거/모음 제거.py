import re
def solution(my_string):
    return re.sub("[aeiou]", "", my_string)