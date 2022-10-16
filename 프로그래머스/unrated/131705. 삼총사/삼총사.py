def solution(number):
    answer = 0
    i, j, k = 0, 1, 2
    
    while i < len(number) - 2:
        if number[i] + number[j] + number[k] == 0:
            answer += 1
            
        if k == len(number) - 1:
            if j == len(number) - 2:
                i += 1
                j = i + 1
                k = i + 2
        
            else:
                j += 1
                k = j + 1
        else:
            k += 1    
                
    return answer