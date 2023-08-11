def solution(sides):
    answer = 0
    min_len, max_len = min(sides), max(sides) 
    for i in range(0, max_len + 1): #sides의 max가 가장 긴 edge일 경우
        if i + min_len > max_len:
            answer += 1

    
    for i in range(max_len + 1, max_len + min_len + 1): # 나머지가 가장 긴 edge일 경우 
        if i < max_len + min_len:
            answer += 1

    return answer