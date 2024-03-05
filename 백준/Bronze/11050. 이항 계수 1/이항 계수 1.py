import sys
import math

a, b = map(int, sys.stdin.readline().split())
answer = math.factorial(a) // (math.factorial(b) * math.factorial(a - b))

print(answer)

    
    
