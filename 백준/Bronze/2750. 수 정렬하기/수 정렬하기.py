import sys

def solution():
    arr= []
    for _ in range(t):
        arr.append(int(sys.stdin.readline()))
        
    arr.sort()
    for i in arr:
        print(i)
t = int(sys.stdin.readline())
solution()