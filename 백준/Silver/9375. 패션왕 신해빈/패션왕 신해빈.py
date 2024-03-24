import sys    
from collections import Counter

test = int(sys.stdin.readline())
for _ in range(test):
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        arr.append(b)
    cnt = Counter(arr)
    answer = 1
    for i in cnt.values():
        answer *= (i + 1)
        
    print(answer - 1)