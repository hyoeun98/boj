def solution(ingredient):
    answer = 0
    idx = 0
    hamburger = [1,2,3,1]
    while len(ingredient) >= idx + 4:
        if ingredient[idx:idx+4] == hamburger:
            del ingredient[idx:idx+4]
            idx = max(0, idx-3)
            answer += 1
        else:
            idx += 1
        
    return answer