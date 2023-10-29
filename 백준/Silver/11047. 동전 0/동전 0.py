import sys

def solution(n, k):
    coins = []
    answer  = 0
    for _ in range(n):
        coins.append(int(sys.stdin.readline()))
    
    while k != 0:
        a, b = divmod(k, coins[-1])
        if a == 0:
            del coins[-1]
        else:
            answer += a
            k = b
            
    

    print(answer)
    
n, k = map(int, sys.stdin.readline().split())
solution(n, k)