import sys

def solution(start):
    if len(answer) == m:
        if tuple(answer) not in visited:
            print(*answer)
            visited.add(tuple(answer))
        return

    for i in range(start, n):
        answer.append(arr[i])
        solution(i + 1)
        answer.pop()
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
visited = set()
answer = []
solution(0)
