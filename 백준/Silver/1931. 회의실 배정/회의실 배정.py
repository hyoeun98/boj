import sys    

n = int(sys.stdin.readline())
meetings = []
answer = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    meetings.append((a, b))

meetings.sort(key = lambda x: (x[1], x[0]))
current_meeting = (0, 0)

for start, end in meetings:
    if current_meeting[1] <= start:
        answer += 1
        current_meeting = (start, end)
        
print(answer)
