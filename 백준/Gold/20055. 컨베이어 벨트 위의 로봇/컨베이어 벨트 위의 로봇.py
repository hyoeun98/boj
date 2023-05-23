import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
A = deque(map(int, sys.stdin.readline().split()))
robots = deque([0 for i in range(N)])

answer = 0
while A.count(0) < K:
    answer += 1
    
    A.rotate(1)
    robots.rotate(1)
    robots[-1] = 0
    
    for i in range(N-2, -1, -1):
        if robots[i] == 1 and robots[i+1] == 0 and A[i+1] > 0:
            robots[i+1] = 1
            A[i+1] -= 1
            robots[i] = 0
            robots[-1] = 0
        
    if robots[0] == 0 and A[0] > 0: # 1번 칸에 로봇이 없음
        robots[0] = 1
        A[0] -= 1
    
print(answer)