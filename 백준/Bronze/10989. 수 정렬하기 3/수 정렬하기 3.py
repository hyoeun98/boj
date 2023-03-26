import sys
from collections import defaultdict

N = int(sys.stdin.readline())
numbers = defaultdict(int)
for _ in range(N):
    numbers[int(sys.stdin.readline())] += 1
    
for i in sorted(numbers.keys()):
    for _ in range(numbers[i]):
        print(i)
