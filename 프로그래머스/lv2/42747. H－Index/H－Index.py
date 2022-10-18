from collections import Counter
def solution(citations):
    paper_cnt = Counter(citations)
    ref = 0
    
    for i in range(max(paper_cnt.keys()), -1, -1):
        ref += paper_cnt[i]
        if ref >= i:
            return i