import sys

def solution():
    if len(answer) == m:
        if tuple(answer) not in visited:
            print(*answer)
            visited.add(tuple(answer))
        return
    
    for i in arr:
        answer.append(i)
        solution()
        answer.pop()
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
answer = []
visited = set()
solution()
