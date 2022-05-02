N = int(input())
ans = ''

while N != 0:
    if N % -2 != 0:
        ans = '1' + ans
        N = N // -2 + 1
    else:
        ans = '0' + ans
        N = N // -2
    
print(ans if ans else 0)
