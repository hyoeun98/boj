import sys
from collections import deque, defaultdict
n, m = map(int, sys.stdin.readline().split())
answer = []
students = [0 for i in range(n + 1)]
topology_dict = defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    students[b] += 1
    topology_dict[a].append(b)

queue = deque()
students[0] = -1
for i, v in enumerate(students):
    if v == 0:
        queue.append(i)
        
while queue:
    node = queue.popleft()
    answer.append(node)
    for i in topology_dict[node]:
        students[i] -= 1
        if students[i] == 0:
            queue.append(i)
print(*answer)