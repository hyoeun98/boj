import sys
a = int(sys.stdin.readline())
x = int(sys.stdin.readline())

binary_x = bin(x)[2:]
answer = 1
dp = [0 for _ in range(len(binary_x))]
expo = 0
dp[0] = a
while expo < len(dp) - 1:
    expo += 1
    dp[expo] = (dp[expo - 1] % 1_000_000_007) * (dp[expo - 1] % 1_000_000_007) % 1_000_000_007

for i, v in enumerate(reversed(binary_x)):
    if v == "0":
        dp[i] = 0
    else:
        answer *= dp[i]

print(answer % 1_000_000_007)