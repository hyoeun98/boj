def solution(s):
    answer = list(map("".join, [[i[idx].upper() if idx % 2 == 0 else i[idx].lower() for idx in range(len(i))] for i in s.split(" ")]))
    
    return " ".join(answer)