import re
def solution(babbling):
    answer = 0
    pronounce = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in pronounce:
            i = re.sub(j, " ", i)
        if not i.strip():
            answer += 1
    return answer