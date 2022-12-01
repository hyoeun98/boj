from collections import Counter
def solution(topping):
    answer = 0
    front, back = set(topping[:1]), Counter(topping[1:])
    back_number = len(back)
    for i in range(1, len(topping)):
        front.add(topping[i])
        back[topping[i]] -= 1
        if back[topping[i]] == 0: back_number -= 1
        if len(front) == back_number:
            answer += 1
        
    return answer