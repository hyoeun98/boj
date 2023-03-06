def solution(n, m, section):
    answer = 0
    
        
    while section:
        current = section[0]
        for i in section[:]:
            if i < m + current:
                section.remove(i)
            else:
                break
        answer += 1
    return answer