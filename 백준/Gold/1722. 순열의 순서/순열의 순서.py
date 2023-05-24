import sys
import math
N = int(sys.stdin.readline())
quiz, *K = map(int, sys.stdin.readline().split())

if quiz == 1:
    answer = []
    K = K[0] - 1
    candidate = list(range(1, N + 1))
    N_factorial = math.factorial(N)
    
    while N != 0:
        answer.append(candidate.pop(K // (N_factorial // N)))
        K %= N_factorial // N
        N_factorial //= N
        N -= 1
    
    print(*answer)
    
else:
    answer = 1
    N_factorial = math.factorial(N)
    candidate = list(range(1, N + 1))

    for i in K:
        answer += candidate.index(i) * (N_factorial // N)
        candidate.pop(candidate.index(i))
        N_factorial //= N
        N -= 1
        
    print(answer)
    