import sys

N = int(sys.stdin.readline())
is_find = False
for i in range(1, N):
     decom = list(str(i))
     candidate = i + sum(map(int, decom))
     if candidate == N:
        is_find = True
        print(i)
        break

if not is_find:
    print(0)
     
