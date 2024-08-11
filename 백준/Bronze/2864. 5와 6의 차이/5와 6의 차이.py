import sys

a, b = sys.stdin.readline().split()

min_answer = int(a.replace("6", "5")) + int(b.replace("6", "5"))
max_answer = int(a.replace("5", "6")) + int(b.replace("5", "6"))

print(min_answer, max_answer)