import itertools as it
def solution(relation):
    answer = 0
    relation = list(zip(*relation))
    candidate = []
    
    for offset in range(1, len(relation) + 1):
        if offset > len(relation):
            break
        comb = list(it.combinations(range(len(relation)), offset))
        
        for i in comb:
            t_tuple = [relation[j] for j in i]
            t_tuple = list(zip(*t_tuple))

            if len(set(t_tuple)) == len(t_tuple):
                candidate.append(set(i))
                
    while candidate:
        sub = candidate[0]
        for i in candidate[:]:
            if i >= sub:
                candidate.remove(i)
        answer += 1
    return answer