import sys

n, score, p = map(int, sys.stdin.readline().split())
if n == 0:
    print(1)
    exit()
    
score_list = list(map(int, sys.stdin.readline().split()))
score_list = score_list[:p]

if score_list[-1] > score:
    if n == p:
        print(-1)
    else:
        print(n + 1)
elif score_list[-1] == score and n == p:
    print(-1)
else:
    for i, v in enumerate(score_list):
        if v > score:
            continue
        else:
            print(i + 1)
            exit()
            
    print(-1)