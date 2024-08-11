import sys

s, k = sys.stdin.readline().split()
s = s.lower()
k = int(k)
answer = []
duplicate = dict()
current = s[0]
cnt = 1
for i in s[1:]:
    if current == i:
        cnt += 1
    else:
        if current not in duplicate.keys():
            duplicate[current] = cnt
        
        cnt = 1
        current = i

if s[-1] not in duplicate.keys():
    if s[-1] == s[-2]:
        duplicate[s[-1]] = cnt + 1
    else:
        duplicate[s[-1]] = 1
    
for i in duplicate.values():
    if i >= k:
        print(1, end = "")
    else:
        print(0, end = "")