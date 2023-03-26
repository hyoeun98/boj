import sys

N = int(sys.stdin.readline())
result = 0
for i in range(1, N):
    decom = str(i)
    candidate = i + sum(map(int, decom))
    if candidate == N:
        result = i
        break

print(result)
     
