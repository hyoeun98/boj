import sys

while True:
    try:
        width = int(sys.stdin.readline()) * 10000000
        n = int(sys.stdin.readline())
        arr = []
        for _ in range(n):
            arr.append(int(sys.stdin.readline()))
        arr.sort()
        start, end = 0, n - 1
        flag = True
        while start < end:
            if arr[start] + arr[end] == width:
                print("yes", arr[start], arr[end])
                flag = False
                break
            if arr[start] + arr[end] < width:
                start += 1
            elif arr[start] + arr[end] > width:
                end -= 1
                
        if flag:
            print("danger")
            
    except:
        break