import sys
N = int(sys.stdin.readline())
words = set()
for _ in range(N):
    words.add(sys.stdin.readline().strip())

words = list(words)
words.sort()
words.sort(key = lambda x: len(x))
for i in words:
    print(i)