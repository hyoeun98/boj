import sys

n = int(sys.stdin.readline())
roads = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

answer = 0
answer += roads[0] * prices[0]
lowest_price = prices[0]
for i in range(1, n - 1):
    if prices[i] < lowest_price:
        lowest_price = prices[i]
    answer += lowest_price * roads[i]

print(answer)