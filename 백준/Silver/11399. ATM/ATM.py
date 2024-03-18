import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

p.sort()
answer = 0
temp = 0
for i in range(n):
    
    temp += p[i]
    answer += temp

print(answer)
