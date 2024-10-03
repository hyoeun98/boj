import sys

n = int(sys.stdin.readline())
arr = list(map(int, (sys.stdin.readline().split())))
reversed_arr = arr[:]
answer = 0
for current in range(1, n):
    pre = current - 1
    while arr[current] < arr[pre]:
        answer += 1
        arr[current], arr[pre] = arr[pre], arr[current]
        if pre == 0:
            break
        current -= 1
        pre -= 1
        
reverse_answer = 1
for current in range(1,n ):
    pre = current - 1
    while reversed_arr[current] > reversed_arr[pre]:
        reverse_answer += 1
        reversed_arr[current], reversed_arr[pre] = reversed_arr[pre], reversed_arr[current]
        if pre == 0:
            break
        current -= 1
        pre -= 1
print(min(answer, reverse_answer))