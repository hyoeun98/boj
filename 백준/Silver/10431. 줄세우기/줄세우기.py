import sys

def solve(arr):
    answer = 0
    line = [arr[0]]
    for i in arr[1:]:
        if i > max(line):
            line.append(i)
        else:
            for j, v in enumerate(line):
                if v > i:
                    answer += len(line) - j
                    line.insert(j, i)
                    break
                
    return answer
p = int(sys.stdin.readline())
for _ in range(p):
    t, *arr = map(int, sys.stdin.readline().split())
    answer = solve(arr)
    print(t, answer)