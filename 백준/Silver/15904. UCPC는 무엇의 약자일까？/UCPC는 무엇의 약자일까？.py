import sys

n = sys.stdin.readline().strip()
a = n.find("U")
b = n.find("C", a)
c = n.find("P", b)
d = n.find("C", c)
if a < b < c < d:
    print("I love UCPC")
else:
    print("I hate UCPC")