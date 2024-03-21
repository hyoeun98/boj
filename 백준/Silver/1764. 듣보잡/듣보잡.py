import sys

n, m = map(int, sys.stdin.readline().split())
answer = []
dup = set()
for _ in range(n):
    dup.add(sys.stdin.readline().strip())
    
for _ in range(m):
    if (temp := sys.stdin.readline().strip()) in dup:
        answer.append(temp) 

answer.sort()
print(len(answer))
for i in answer:
    print(i)