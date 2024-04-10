import sys

n = int(sys.stdin.readline())
ch = []
answer = []
for i in range(1, n + 1):
    temp = sys.stdin.readline().strip()
    if temp == "KBS1":
        kbs1 = i
    elif temp == "KBS2":
        kbs2 = i
    ch.append(temp)
    
answer.append("1" * (kbs1 - 1))
answer.append("4" * (kbs1 - 1))
if kbs1 > kbs2:
    kbs2 += 1
    
answer.append("1" * (kbs2 - 1))
answer.append("4" * (kbs2 - 2))
print("".join(answer))
