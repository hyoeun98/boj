import sys

def bin_search(A, target):
    start = 0
    end = len(A) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if A[mid] == target:
            return True
        elif A[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return False

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()
for i in B:
    if bin_search(A, i):
        print(1)
    else:
        print(0)
            