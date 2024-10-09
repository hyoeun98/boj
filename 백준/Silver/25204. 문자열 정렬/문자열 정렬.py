import sys
from functools import cmp_to_key

def compare(x, y):
    if x == y:
        return 0
    elif x.startswith(y):
        return 1
    elif y.startswith(x):
        return -1
    else:
        for i, j in zip(x, y):
            if i != j:
                if not i.isalpha():
                    return 1
                elif not j.isalpha():
                    return -1
                else:
                    if i.lower() < j.lower():
                        return -1
                    elif i.lower() > j.lower():
                        return 1
                    else:
                        if i.islower():
                            return 1
                        else:
                            return -1
                        
                    
        
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        word = sys.stdin.readline().strip().replace("-", "~")
        arr.append(word)
    
    arr.sort(key=cmp_to_key(compare))
    for i in arr:
        print(i.replace("~", "-"))