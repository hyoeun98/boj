from collections import Counter
def solution(before, after):
    before_cnt = Counter(before)
    after_cnt = Counter(after)
    
    return 1 if before_cnt == after_cnt else 0