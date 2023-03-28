import sys
import itertools as it

N, M = map(int, (sys.stdin.readline().split()))
answer = M
numbers = list(map(int, sys.stdin.readline().split()))
comb = it.combinations(numbers, 3)
for i in comb:
    if M - sum(i) >= 0:
        answer = min(answer, M - sum(i))

print(M - answer)
