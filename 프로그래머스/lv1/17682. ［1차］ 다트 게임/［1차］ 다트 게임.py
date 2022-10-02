def solution(dartResult):
    dartResult = dartResult.replace("10","A")
    score, bonus, option = [], [], []
    bonus_dict = {"S" : 1, "D" : 2, "T" : 3}
    answer = 0    
    
    for idx in range(len(dartResult)):
        if dartResult[idx].isdigit() or dartResult[idx] == "A":
            score.append(int(dartResult[idx], 16))
            
        elif dartResult[idx] in ["S", "D", "T"]:
            bonus.append(dartResult[idx])
            if idx + 1 < len(dartResult) and dartResult[idx + 1] in ["*", "#"]:
                option.append(dartResult[idx + 1])
            else:
                option.append(' ')
            
    for idx in range(len(score)):
        score[idx] **= bonus_dict[bonus[idx]]
        if option[idx] == "#":
            score[idx] *= -1
        elif option[idx] == "*":
            score[idx] *= 2
            if idx != 0:
                score[idx - 1] *= 2
        
    return sum(score)