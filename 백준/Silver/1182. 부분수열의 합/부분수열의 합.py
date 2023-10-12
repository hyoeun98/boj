import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0

def back_tracking(sub_sum, idx):
    global answer
    if idx >= n:
        return
    sub_sum += arr[idx]
    if sub_sum == s:
        answer += 1
        
    back_tracking(sub_sum, idx + 1)
    back_tracking(sub_sum - arr[idx], idx + 1)

def solution():
    back_tracking(0, 0)
    print(answer)
    
    
    

solution()