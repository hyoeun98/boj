import sys
    
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
lights = list(map(int, sys.stdin.readline().split()))
start, end = 1, n
mid = (start + end) // 2
while start <= end:
    flag = False
    if lights[0] - mid > 0:
        start = mid + 1
        mid = (start + end) // 2
        continue
    lights_start, lights_end = max(0, lights[0] - mid), min(lights[0] + mid, n)
    for i in lights[1:]:
        next_lights_start, next_lights_end = max(0, i - mid), min(i + mid, n)
        if next_lights_start > lights_end:
            flag = True
            break
        else:
            lights_start, lights_end = next_lights_start, next_lights_end
    if lights_end < n:
        flag = True
    
    if flag:
        start = mid + 1
    else:
        end = mid - 1

    mid = (start + end) // 2
print(start)