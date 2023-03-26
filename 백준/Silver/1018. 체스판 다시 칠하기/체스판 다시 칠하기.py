import sys

def check_board(board, dx, dy):
    cnt = 0
    first = board[dy][dx]
    for y in range(dy, dy + 8):
        for x in range(dx, dx + 8):
            if y == 0 and x == 0: 
                continue
            if first == board[y][x]:
                cnt += 1
            else:
                pass
            first = 'W' if first != 'W' else 'B'
        first = 'W' if first != 'W' else 'B'
        
    return min(cnt, 64 - cnt)

N, M = map(int, sys.stdin.readline().split())
board = []
answer = 64
for _ in range(N):
    board.append(sys.stdin.readline().strip())
    
for dy in range(N-7):
    for dx in range(M-7):
        answer = min(answer, check_board(board, dx, dy))
        
        
print(answer)
            