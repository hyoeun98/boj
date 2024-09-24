import sys

n, l = map(int, sys.stdin.readline().split())
flag = True
while flag:
    if (l * (l - 1) // 2) > n:
        break
    
    i = max(0, n // l - l // 2 - 1)
    temp = i * l + (l * (l - 1) // 2)
    if temp == n:
        answer = [a for a in range(i, i + l)]
        flag = False
        break
    
    i += 1
    temp = i * l + (l * (l - 1) // 2)
    if temp == n:
        answer = [a for a in range(i, i + l)]
        flag = False
        break
    
    i += 1
    temp = i * l + (l * (l - 1) // 2)
    if temp == n:
        answer = [a for a in range(i, i + l)]
        flag = False
        break
    
    l += 1
    
if flag:
    print(-1)
else:
    if len(answer) > 100:
        print(-1)
    else:
        print(*answer)