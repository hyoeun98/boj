import sys

while True:
    answer = 0
    a, b = sys.stdin.readline().split()
    if a == "0" and b == "0":
        break
    if len(a) > len(b):
        b = (len(a) - len(b)) * "0" + b
    elif len(a) < len(b):
        a = (len(b) - len(a)) * "0" + a
        
    cnt = 0
    for i in range(len(a)- 1, -1, -1):
        if int(a[i]) + int(b[i]) + cnt >= 10:
            answer += 1
            cnt = 1
        else:
            cnt = 0
    
    print(answer)
        
    
    