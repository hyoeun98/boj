import sys

n, k = map(int, sys.stdin.readline().split())
answer = []
arr = list(range(1, n+1))
current = 0
while arr:
    current += k - 1
    current %= len(arr)
        
    answer.append(str(arr.pop(current)))
        
print(f"<{', '.join(answer)}>")