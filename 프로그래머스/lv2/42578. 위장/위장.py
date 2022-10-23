from collections import defaultdict
import itertools as it
import math
def solution(clothes):
    clothes_dict = defaultdict(lambda : 1)
    for i in clothes:
        clothes_dict[i[1]] += 1
    
    return math.prod(clothes_dict.values()) - 1