import sys        
import itertools as it

def solution():
    arr = list(it.permutations(range(1, n + 1), m))
    for i in arr:
        print(*i)
    
n, m = map(int, sys.stdin.readline().split())
solution()
