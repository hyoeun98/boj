import sys

s = sys.stdin.readline().strip()
p, k, h, t = 13, 13, 13, 13
arr = []
flag = False
for i in range(0, len(s), 3):
    card = s[i: i+3]
    if card in arr:
        flag = True
        break
    else:
        arr.append(card)
        shape = card[0]
        if shape == "P":
            p -= 1
        elif shape == "K":
            k -= 1
        elif shape == "H":
            h -= 1
        else:
            t -= 1
            
if flag:
    print("GRESKA")
else:
    print(p, k, h, t)