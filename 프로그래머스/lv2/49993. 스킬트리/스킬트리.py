def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        valid_check = -2
        for offset, j in enumerate(skill):
            idx = i.find(j)
            if (valid_check > idx and idx != -1) or (valid_check < idx and valid_check == -1):
                # print(i, j)
                answer -= 1
                break
            valid_check = idx
        answer += 1
    return answer