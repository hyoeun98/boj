import sys

n = int(sys.stdin.readline())
board = []
for _ in range(n):
    board.append(sys.stdin.readline().strip())
    
for i, v in enumerate(board):
    if (head := v.find("*")) != -1:
        head = i + 1, head + 1
        heart = head[0] + 1, head[1]
        break

arms = board[heart[0] - 1]
left_arm = arms[:heart[1] - 1].count("*")
right_arm = arms[heart[1]:].count("*")

h = 0
for i in board[heart[0]:]:
    if i[heart[1] - 1] == "*":
        h += 1
    else:
        break
left_leg, right_leg = 0, 0
for i in board[heart[0] + h:]:
    if i[heart[1] - 2] == "*":
        left_leg += 1
    if i[heart[1]] == "*":
        right_leg += 1
        
print(heart[0], heart[1])
print(left_arm, right_arm, h, left_leg, right_leg)
    
    