def solution(arr):
    for i in range(len(arr) -1):
        x, y = arr[i], arr[i+1]
        while y != 0:
            x, y = y, x%y

        arr[i+1] = arr[i] * arr[i+1] // x
    
    return arr[-1]