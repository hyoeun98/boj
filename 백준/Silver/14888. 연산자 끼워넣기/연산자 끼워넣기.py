import sys

maximum = -1e10
minimum = 1e10
def dfs(count, result, plus, minus, mul, div):
    global maximum, minimum
    if count == n:
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return
    
    if plus:
        dfs(count + 1, result + arr[count], plus - 1, minus, mul, div)
    if minus:
        dfs(count + 1, result - arr[count], plus, minus - 1, mul, div)
    if mul:
        dfs(count + 1, result * arr[count], plus, minus, mul - 1, div)
    if div:
        dfs(count + 1, int(result / arr[count]), plus, minus, mul, div - 1)
    
    
n = int(sys.stdin.readline())
arr = list(map(int ,sys.stdin.readline().split()))
operations = list(map(int ,sys.stdin.readline().split()))
dfs(1, arr[0], *operations)
print(maximum)
print(minimum)
