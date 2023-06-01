import sys

W, H, f, c, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

answer = W * H

if W/2 >= f: # f에 맞춰 접을 때 f가 W의 절반 이하
    row = f
        
else: # f가 W의 절반보다 큼
    row = W - f

if row <= x1:
    answer -= (c + 1) * (y2 - y1) * (x2 - x1)

elif row < x2:
    answer -= 2 * (c + 1) * (y2 - y1) * (row - x1)
    answer -= (c + 1) * (y2 - y1) * (x2 - row)
else:
    answer -= 2 * (c + 1) * (y2 - y1) * (x2 - x1)

print(answer)