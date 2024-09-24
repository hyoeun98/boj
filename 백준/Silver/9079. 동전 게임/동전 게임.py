import sys
from collections import deque
import copy
def board_to_binary(board):
    binary = 0
    cnt = 8
    for i in board:
        for j in i:
            binary += j * (2 ** cnt)
            cnt -= 1
    return binary

def binary_to_board(binary):
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    cnt = 8
    for i in range(3):
        for j in range(3):
            if binary >= 2 ** cnt:
               board[i][j] = 1
               binary -= 2 ** cnt
            cnt -= 1
     
    return board
def flip(board):
    flip_case = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    flipped_board = []
    for i in flip_case:
        temp = copy.deepcopy(board)
        for j in i:
            if temp[j // 3][j % 3] == 0:
                temp[j // 3][j % 3] = 1
            else:
                temp[j // 3][j % 3] = 0
    
        flipped_board.append(board_to_binary(temp))
        
    return flipped_board
                
    
def solve(board):
    visited = [False for _ in range(512)]
    queue = deque()
    
    binary = board_to_binary(board)
    visited[binary] = True
    queue.append((binary, 0))
    
    while queue:
        current_board, cnt = queue.popleft()
        if current_board == 0 or current_board == 511:
            print(cnt)
            return
        
        temp = flip(binary_to_board(current_board))
        
        for i in temp:
            if not visited[i] and i not in [i[0] for i in queue]:
                visited[i] = True
                queue.append((i, cnt + 1))
                
    print(-1)
    
n = int(sys.stdin.readline())
for _ in range(n):
    board = []
    for _ in range(3):
        t = sys.stdin.readline().split()
        t = [1 if i == "H" else 0 for i in t]
        board.append(t)
        
    solve(board)
