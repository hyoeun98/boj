import sys    
import math
t = int(sys.stdin.readline())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    k = x
    lcm = math.lcm(m, n)
    flag = True
    while k <= lcm:
        if (k - x) % m == 0 and (k - y) % n == 0:
            print(k)
            flag = False
            break

        else:
            k += m

    if flag:
        print(-1)