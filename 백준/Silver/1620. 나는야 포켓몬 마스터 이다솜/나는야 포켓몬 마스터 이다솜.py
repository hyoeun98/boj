import sys    

n, m = map(int,sys.stdin.readline().split())
pocketmon_dict = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    pocketmon_dict[str(i + 1)] = name
    pocketmon_dict[name] = str(i + 1)
    
for i in range(m):    
    print(pocketmon_dict[sys.stdin.readline().strip()])