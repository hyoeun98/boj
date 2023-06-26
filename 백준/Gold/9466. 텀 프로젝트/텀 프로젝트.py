import sys
from collections import deque
sys.setrecursionlimit(1000000)
# def search(current_student, next_student):
#     global answer
#     group = deque()

#     while True:
#         group.append(current_student)
#         if next_student in group:
#             idx = group.index(next_student)
#             answer -= len(group) - idx
#             visit.update(group)
#             break

#         elif next_student in visit:
#             visit.update(group)
#             break

#         current_student, next_student = next_student, students[next_student - 1]

def dfs(current_student, next_student):
    global answer
    visit[current_student] = True
    group.append(current_student)
    
    if visit[next_student]:
        if next_student in group:
            idx = group.index(next_student)
            answer -= len(group) - idx
        return
    else:
        dfs(next_student, students[next_student - 1])

T = int(sys.stdin.readline())

for ans in range(T):
    n = int(sys.stdin.readline())
    students = list(map(int, sys.stdin.readline().split()))
    answer = n
    visit = [False for _ in range(n+1)] 
    for i, v in enumerate(students):
        if not visit[i+1]:
            group = []
            dfs(i + 1, v)
    print(answer)