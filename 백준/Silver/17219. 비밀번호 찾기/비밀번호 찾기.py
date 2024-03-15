import sys

n, m = map(int, sys.stdin.readline().split())
account_dict = dict()
for _ in range(n):
    id, pwd = sys.stdin.readline().split()
    account_dict[id] = pwd
    
for _ in range(m):
    print(account_dict[sys.stdin.readline().strip()])