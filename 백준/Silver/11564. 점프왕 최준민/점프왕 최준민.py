import sys

k, a, b = map(int, sys.stdin.readline().split())
answer = 0
if a == 0 or b == 0 or (a < 0 and b > 0):
    answer = 1
    answer += abs(a) // k
    answer += b // k


else:
    a, b = abs(a), abs(b)
    if a > b:
        a, b = b, a
    if k > b:
        answer = 0
        
    elif k > a:
        answer = b // k

    else: # k < a
        if a % k == 0:
            answer = b // k - a // k + 1
        else:
            answer = b // k - a // k

print(answer)