import sys

def solve(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (solve(a, b // 2, c) ** 2) % c
    else:
        return ((solve(a, b // 2, c) ** 2) * a) % c
a, b, c = map(int, sys.stdin.readline().split())

print(solve(a, b, c))