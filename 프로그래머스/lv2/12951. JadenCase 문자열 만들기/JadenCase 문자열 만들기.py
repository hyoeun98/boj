def solution(s):
    s = s[0].upper() + s[1:]
    answer = s[0]
    
    for idx in range(1, len(s)):
        if s[idx].isalpha():
            if s[idx - 1] == " ":
                t = s[idx].upper()
            else:
                t = s[idx].lower()
        else:
            t = s[idx]
        answer += t
            
    return answer