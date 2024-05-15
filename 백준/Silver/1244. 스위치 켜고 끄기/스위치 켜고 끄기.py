import sys

n = int(sys.stdin.readline())
switches = [-1] + list(map(int, sys.stdin.readline().split()))
students = int(sys.stdin.readline())
student_list = []
for _ in range(students):
    student_list.append(list(map(int, sys.stdin.readline().split())))
    
for i in student_list:
    sex, num = i
    cnt = num
    if sex == 1: # 남자
        while num <= n:
            if switches[num] == 1:
                switches[num] = 0
            else:
                switches[num] = 1
            num += cnt
    else: # 여자
        start, end = num, num
        while start - 1 > 0 and end + 1 <= n:
            if switches[start - 1] == switches[end + 1]:
                start -= 1
                end += 1
            else:
                break
        for i in range(start, end + 1):
            if switches[i] == 1:
                switches[i] = 0
            else:
                switches[i] = 1
                
        
for i, v in enumerate(switches[1:]):
    print(v, end = " ")
    if (i + 1) % 20 == 0:
        print()