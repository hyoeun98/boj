import sys

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    t = list(map(int, sys.stdin.readline().split()))
    board.append(t)
    
dp = [[i[:] for _ in range(3)] for i in board]

for i, row in enumerate(dp):
    if i == 0: continue

    for direction, element in enumerate(row): #direction 0, 1, 2
        for k in range(m):       
            if direction == 0:
                if k == m - 1:
                    dp[i][direction][k] = dp[i-1][1][k] + board[i][k]    
                else:
                    dp[i][direction][k] = min(dp[i-1][1][k], dp[i-1][2][k+1]) + board[i][k]
                
            elif direction == 1:
                if k == m - 1:
                    dp[i][direction][k] = dp[i-1][0][k-1] + board[i][k]
                elif k == 0:
                    dp[i][direction][k] = dp[i-1][2][k+1] + board[i][k]
                else:
                    dp[i][direction][k] = min(dp[i-1][0][k-1], dp[i-1][2][k+1]) + board[i][k]
                
            elif direction == 2:
                if k == 0:
                    dp[i][direction][k] = dp[i-1][1][k] + board[i][k]
                else:
                    dp[i][direction][k] = min(dp[i-1][0][k-1], dp[i-1][1][k]) + board[i][k]
answer = 1e9
for i in dp[-1]:
    answer = min(answer, min(i))

print(answer)