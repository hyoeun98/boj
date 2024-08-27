import sys

input = sys.stdin.readline().strip()
board = input.split(".")
arr = []
for i in board:
    if len(i) % 2 != 0:
        print(-1)
        exit()
    else:
        if len(i) >= 4:
            arr.extend("AAAA" * (len(i) // 4))
        if len(i) % 4 == 2:
            arr.extend("BB")

for i, v in enumerate(input):
    if v == ".":
        arr.insert(i, ".")
    
answer = "".join(arr)
print(answer)