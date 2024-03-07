import sys
    
n = int(sys.stdin.readline())
arr = []
answer = [0 for _ in range(n)]
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])

for i, a in enumerate(arr):
    current_x, current_y = a
    cnt = 1
    for j, b in enumerate(arr):
        if i == j:
            continue
        comp_x, comp_y = b
        
        if current_x < comp_x and current_y < comp_y:
            cnt += 1
    
    print(cnt)