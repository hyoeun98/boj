def solution(num):
    count = 0
    while count < 500:
        if num == 1:
            return count
        else:
            pass
        
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
            
        count += 1
        
    return -1