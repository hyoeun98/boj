import sys
import math
n = int(sys.stdin.readline())
if math.sqrt(n).is_integer():
    print(-1)
else:
    answer = 0
    for i in range (1,int(math.sqrt(n/2))+1):
        j = n - i**2
        if math.sqrt(j) - int(math.sqrt(j)) == 0:
            answer += 1
        else:
            continue

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0 and (n // i) % 2 == 0:
                answer += 1
            elif i % 2 == 1 and (n // i) % 2 == 1:
                answer += 1
        
    print(answer)