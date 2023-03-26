import sys
input = sys.stdin.readline().strip()
while input != '0':
    if input == (input[::-1]):
        print("yes")
    else:
        print("no")
    input = sys.stdin.readline().strip()