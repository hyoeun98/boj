from collections import Counter

def solution(weights):
    answer = 0
    count = Counter(weights)
    for i in count:
        answer += count[i] * (count[i] - 1) // 2 # 같은 무게
        answer += count[i] * count[i * (3/2)]
        answer += count[i] * count[i * (4/3)]
        answer += count[i] * count[i * 2]
        
            
    
    return answer