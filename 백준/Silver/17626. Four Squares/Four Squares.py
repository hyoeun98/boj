import sys    
import math
n = int(sys.stdin.readline())

dp = [1 if int(math.sqrt(i)) ** 2 == i else 0 for i in range(n + 1)]
dp[0] = 0
for i in range(1, n + 1):
    if dp[i] != 0:
        continue
    else:
        j = 1
        cnt = 4
        while j ** 2 < i:
            cnt = min(cnt, dp[j ** 2] + dp[i - j ** 2])
            j += 1
        dp[i] = cnt

print(dp[n])