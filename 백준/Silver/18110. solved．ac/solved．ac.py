import sys
EPS = 1e-12
n = int(sys.stdin.readline())
if n == 0:
    print(0)
    exit(0)
    
scores = []
for _ in range(n):
    scores.append(int(sys.stdin.readline()))

scores.sort()
num_cut = round(n * 0.15 + EPS)

del scores[n:-num_cut - 1:-1]
del scores[:num_cut]

print(round(sum(scores) / len(scores) + EPS))