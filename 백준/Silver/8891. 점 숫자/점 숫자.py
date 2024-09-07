import sys

def calc(point_num):
    cnt = 1
    while cnt < point_num:
        point_num -= cnt
        cnt += 1
        
    co = [cnt, 1]
    for _ in range(point_num - 1):
        co[0] -= 1
        co[1] += 1
        
    return co
t = int(sys.stdin.readline())

def calc_reverse(y, x):
    answer = 0
    cnt = 0
    while x != 1:
        y += 1
        x -= 1
        cnt += 1
        
    a, b = 1, 1
    for i in range(y - 1):
        a += 1
        b = a + b - 1
    
    print(b + cnt)
for _ in range(t):
    y, x = map(int , sys.stdin.readline().split())
    a, b = calc(y)
    c, d = calc(x)
    answer = (a + c, b + d)
    calc_reverse(*answer)
    