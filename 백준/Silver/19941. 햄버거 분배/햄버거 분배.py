import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().strip())
answer = 0
current = 0
while current < n:
    if arr[current] == "P":
        for i in range(max(0, current - k) , min(current + k + 1, n)):
            if arr[i] == "H":
                arr[i] = -1
                answer += 1
                break
        
    current += 1
    
print(answer)
    
