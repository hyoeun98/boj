import itertools as it
import operator
def solution(num_list):
    summation = sum(num_list)
    multiplication = list(it.accumulate(num_list, operator.mul))[-1]
    return 1 if summation ** 2 > multiplication else 0