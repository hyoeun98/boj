import sys
from collections import deque
# 피사노 주기
n = int(sys.stdin.readline())
cnt = 0
fibo = deque([0, 1])
while cnt < (n - 1) and cnt < 1_500_000:
    cnt += 1
    fibo.append((fibo[-1] + fibo[-2]) % 1_000_000)

print(fibo[n % 1_500_000])