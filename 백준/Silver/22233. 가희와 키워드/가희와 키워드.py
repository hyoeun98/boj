import sys

n, m = map(int, sys.stdin.readline().split())
words = set()
writes = []
for _ in range(n):
    words.add(sys.stdin.readline().strip())
    
for _ in range(m):
    writes.append(sys.stdin.readline().strip().split(","))
    
for i in writes:
    for j in i:
        words.discard(j)
    print(len(words))
