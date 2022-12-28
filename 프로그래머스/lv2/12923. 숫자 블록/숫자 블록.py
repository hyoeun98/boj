import itertools as it
import math
def get_divisor(num):
    divisors = []
    length = int(math.sqrt(num)) + 1
    
    for i in range(2, length):
        if num % i == 0 and num // i <= 10_000_000:
            divisors.append(i)
            divisors.append(num//i)

    divisors.sort()
    return divisors

def solution(begin, end):
    answer = []
    if begin == 1:
        answer.append(0)
        begin = 2
    divisor = list(map(get_divisor, range(begin ,end+1)))
    for i in divisor:
        if i:
            answer.append(list(it.takewhile(lambda x: x<=10_000_000, i))[-1])
        else:
            answer.append(1)
    return answer