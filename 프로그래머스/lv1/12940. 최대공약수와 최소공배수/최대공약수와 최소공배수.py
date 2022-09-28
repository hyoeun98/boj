def solution(n, m):
    answer = []
    min_num = min(n ,m)
    max_num = max(n, m)
    for i in range(min_num, 0, -1):
        if max_num % i == 0 and min_num % i == 0:
            answer.append(i)
            break
    # lcm = abs(ab) / gcd(a, b)
    answer.append(n * m / answer[0]) 
            
    return answer