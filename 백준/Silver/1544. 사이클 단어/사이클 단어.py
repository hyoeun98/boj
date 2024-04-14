import sys
from collections import deque
n = int(sys.stdin.readline())
words = []
for _ in range(n):
    temp = deque(sys.stdin.readline().strip())
    is_same_word = False
    for _ in range(len(temp)):
        if temp in words:
            is_same_word = True
            break
        temp.rotate(1)
    if not is_same_word:
        words.append(temp)
        
print(len(words))