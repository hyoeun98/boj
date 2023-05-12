def solution(myString, pat):
    answer = 0
    for i, v in enumerate(myString):
        if pat == myString[i:i+len(pat)]:
            answer += 1
    return answer