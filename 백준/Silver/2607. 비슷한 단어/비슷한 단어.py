import sys
from collections import Counter

n = int(sys.stdin.readline())
words = []
for _ in range(n):
    words.append(sys.stdin.readline().strip())
    
answer = 0
first = Counter(words[0])
for i in words[1:]:
    t = Counter(i)
    t.subtract(first)
    v = list(t.values())

    if sum(map(abs, v)) < 2 or (v.count(1) == 1 and v.count(-1) == 1 and sum(map(abs, v)) == 2):
        answer += 1        
print(answer)

