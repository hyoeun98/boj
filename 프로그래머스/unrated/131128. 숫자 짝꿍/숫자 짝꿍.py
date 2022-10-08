from collections import Counter
def solution(X, Y):
    X_counter = Counter(X)
    Y_counter = Counter(Y)
    pair_num = {}
    answer = ""
    
    for i in X_counter.keys():
        if i in Y_counter.keys():
            pair_num[i] = min(X_counter[i], Y_counter[i])
    
    if pair_num:
        pair_num_keys = sorted(pair_num.keys(), reverse = True)
        for i in pair_num_keys:
            answer += i * pair_num[i]
        
    else:
        answer = "-1"
    
    return answer if answer[0] != "0" else "0"