import sys

T = int(sys.stdin.readline())

def solution():
    N = int(sys.stdin.readline())
    answer = N
    candidate = [0 for _ in range(N + 1)]
    for _ in range(N):
        a, b= map(int, sys.stdin.readline().split())
        candidate[a] = b
    cand_min = candidate[1]
    for i in range(2, N + 1):
        if cand_min < candidate[i]:
            answer -= 1
        else:
            cand_min = candidate[i]
            
    
    print(answer)
        
for _ in range(T):
    solution()
        