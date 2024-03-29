import sys    

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

answer = 0
start, end = 0, 2
ioi = "IOI"
cnt = 0
while end < m:
    if s[start : end + 1] == ioi:
        start += 2
        end += 2
        cnt += 1
    else:
        start += 1
        end += 1
        cnt = 0
    
    if cnt == n:
        answer += 1
        cnt -= 1

print(answer)    
    