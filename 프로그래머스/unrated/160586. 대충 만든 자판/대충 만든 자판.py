from collections import defaultdict
def solution(keymap, targets):
    answer = []
    key_dict = defaultdict(int)
    for i in keymap:
        for j, v in enumerate(i):
            if v not in key_dict.keys():
                key_dict[v] = j + 1
            else:
                key_dict[v] = min(key_dict[v], j + 1)
    
    for i in targets:
        temp = 0
        for j in i:
            if j in key_dict.keys():
                temp += key_dict[j]
            else:
                temp = 0
                break
            
        answer.append(temp if temp !=0 else -1)
        
    return answer