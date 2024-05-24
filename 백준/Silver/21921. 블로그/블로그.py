import sys

n, x = map(int ,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

if max(arr) == 0:
    print("SAD")
    exit()

aggregate = [0]
for i in arr:
    aggregate.append(aggregate[-1] + i)
    
answer = 0
cnt = 0
for i in range(n - x + 1):
    candidate = aggregate[i + x] - aggregate[i]
    if candidate > answer:
        answer = candidate
        cnt = 1
    elif candidate == answer:
        cnt += 1
        
print(answer)
print(cnt)
    