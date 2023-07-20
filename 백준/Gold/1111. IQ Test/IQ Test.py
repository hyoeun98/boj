import sys

def solution():
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    if len(arr) <= 2:
        if len(arr) == 2 and arr[0] == arr[1]:
            print(arr[0])
            return
        else:
            print("A")
            return
            
    else:
        if arr[0] == arr[1] and arr[1] != arr[2]:
            print("B")
            return

        if arr[0] == arr[1] == arr[2]:
            a, b = 1, 0
        
        else:
            a = (arr[2] - arr[1]) // (arr[1] - arr[0])
            b = arr[1] - (arr[0] * a)

        invalid_flag = False
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1] * a + b:
                invalid_flag = True
                break
        
        print("B" if invalid_flag else arr[-1] * a + b)
        # print(a, b)    
solution()