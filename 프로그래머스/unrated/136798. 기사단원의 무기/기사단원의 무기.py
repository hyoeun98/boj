from collections import Counter
def prime(N):
    p = []
    if(N != 1):
        for i in range(2,int(N**0.5)+1):
            while (N % i == 0):
                p.append(i)
                N = N//i

            if N == 1:
                break
    if N != 1:
        p.append(N)
    return Counter(p).values()

def solution(number, limit, power):
    answer = [1]
    for i in range(2, number+1):
        mul = 1
        cnt = list(map(lambda x: x+1, prime(i)))
        for j in cnt:
            mul *= j
        answer.append(mul if mul <= limit else power) 

    return sum(answer)