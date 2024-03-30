import sys    
import math
t = int(sys.stdin.readline())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    current_x, current_y = x, y
    lcm = math.lcm(m, n)
    flag = True
    while current_x <=  lcm and current_y <= lcm:
        if current_x == current_y:
            print(current_x)
            flag = False
            break
        elif current_x > current_y:
            current_y += n
        else:
            current_x += m

    if flag:
        print(-1)