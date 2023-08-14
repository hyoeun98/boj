import sys

def check(num, weight):
    if num > n_weights:
        return

    if dp[num][weight] == 1:
        return

    dp[num][weight] = 1

    check(num + 1, weight)
    check(num + 1, weight + weights[num - 1])
    check(num + 1, abs(weight - weights[num-1]))

def solution():
    check(0, 0)
    for ball in balls:
        if ball > weights[-1] * n_weights:
            print("N", end = " ")
            continue
        if dp[n_weights][ball] == 1:
            print("Y", end = " ")
        else:
            print("N", end = " ")

n_weights = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))
n_balls = int(sys.stdin.readline())
balls = list(map(int, sys.stdin.readline().split()))
dp = [[0 for j in range((i + 1) * 500 + 1)] for i in range(n_weights + 1)]

solution()
