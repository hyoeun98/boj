import sys

n = int(sys.stdin.readline())
n %= 100
if n <= 10:
    if n == 0 or n == 10:
        print(0)
    else:
        print(1)
elif n <= 30:
    if n == 30:
        print(0)
    elif n <= 15 or n >= 25:
        print(1)
    else:
        print(2)
elif n <= 60:
    if n == 60:
        print(0)
    elif n <= 35 or n >= 55:
        print(1)
    elif n <= 40 or n >= 50:
        print(2)
    else:
        print(3)
elif n <= 100:
    if n == 100:
        print(0)
    elif n <= 65 or n >= 95:
        print(1)
    elif n <= 70 or n >= 90:
        print(2)
    elif n <= 75 or n >= 85:
        print(3)
    else:
        print(4)