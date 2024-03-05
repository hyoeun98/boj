import sys
from collections import Counter
n = int(sys.stdin.readline())
numbers = Counter(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
cnt_nums = list(map(int, sys.stdin.readline().split()))

for i in cnt_nums:
    print(numbers[i], end = " ")