import sys
import re

while True:
    pw = sys.stdin.readline().strip()
    if pw == "end":
        break
    if not re.findall("[aeiou]", pw):
        print(f"<{pw}> is not acceptable.")
        continue
    flag = False
    stack = 1
    prev = pw[0]
    for i in pw[1:]:
        if (i != "e" and i != "o") and i == prev:
            print(f"<{pw}> is not acceptable.")
            flag = True
            break
        if prev in "aeiou":
            if i in "aeiou":
                stack += 1
            else:
                stack = 1
        elif prev not in "aeiou":
            if i not in "aeiou":
                stack += 1
            else:
                stack = 1
        prev = i
        if stack >= 3:
            print(f"<{pw}> is not acceptable.")
            flag = True
            break
    if flag:
        continue
    
    print(f"<{pw}> is acceptable.")
