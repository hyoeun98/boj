import sys

def solution():
    
    arr = [a, b, c]
    arr.sort()
    if arr[2] >= arr[0] + arr[1]:
        print("Invalid")
        return

    d = set(arr)
    length = len(d)
    if length == 1:
        print("Equilateral")
    elif length == 2:
        print("Isosceles")
    elif length == 3:
        print("Scalene")

while True:
    a, b, c = map(int ,sys.stdin.readline().split())
    if a == b == c == 0:
        break
    else:
        solution()

