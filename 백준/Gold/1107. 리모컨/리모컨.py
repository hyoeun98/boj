import sys

n = int(sys.stdin.readline()) 
m = int(sys.stdin.readline())
if m != 0:
    buttons = sys.stdin.readline().split()
else:
    buttons = []
answer = abs(100 - n)
for i in range(1000001):
    for j in str(i):
        if j in buttons:
            break
    else:
        answer = min(answer, abs(n - i) + len(str(i)))
        
print(answer)