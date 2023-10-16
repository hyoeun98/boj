import sys

def solution():
    if len(answer) == m:
        temp = []
        for idx in answer:
            temp.append(arr[idx])
        if tuple(temp) not in visited:
            print(*temp)
            visited.add(tuple(temp))
        return

    
    for i in range(n):
        if i not in answer:
            answer.append(i)
            solution()
            answer.pop()

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
visited = set()
answer = []
solution()
