import sys

n = int(sys.stdin.readline())
arr = []
answer = [0, 0, 0]
for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    arr.append((a, b, c))
    
arr.sort(key = lambda x: x[2], reverse = True)
answer[0] = arr[0]
answer[1] = arr[1]
if answer[0][0] != answer[1][0]:
    answer[2] = arr[2]
else:
    for a, b, c in arr[2:]:
        if answer[1][0] != a:
            answer[2] = (a, b, c)
            break
    
for i in answer:
    print(i[0], i[1])