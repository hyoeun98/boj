import sys

s = list(sys.stdin.readline().strip())
for _ in range(s.count("1") // 2):
    s.remove("1")
    
s = list(reversed(s))
for _ in range(s.count("0") // 2):
    s.remove("0")
    
s = list(reversed(s))
print("".join(s))