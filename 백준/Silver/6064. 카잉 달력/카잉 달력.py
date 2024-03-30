import sys    
import math

def solve():
    k = x
    lcm = math.lcm(m, n)
    while k <= lcm:
        if (k - x) % m == 0 and (k - y) % n == 0:
            return k

        else:
            k += m

    return -1

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    print(solve())