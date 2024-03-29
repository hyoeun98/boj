import sys    
import re
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
ioi = "IO" * n + "I"
find = list(re.finditer(f'(?=({ioi}))', s))
print(len(find))