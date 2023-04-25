import itertools as it
import operator
def solution(num_list):
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        answer = list(it.accumulate(num_list, operator.mul))[-1]
    return answer