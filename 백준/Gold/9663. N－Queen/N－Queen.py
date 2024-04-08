import sys

def put_check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
        
    return True

def n_queens(x):
    global answer
    if x == n:
        answer += 1
        return
        
    else:
        for i in range(n):
            row[x] = i
            if put_check(x): # x에 놓을 수 있다면
                n_queens(x + 1)

n = int(sys.stdin.readline())
row = [0 for _ in range(n)]
answer = 0

n_queens(0)    
print(answer)
    