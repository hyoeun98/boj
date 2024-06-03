import sys

p, m = map(int ,sys.stdin.readline().split())
rooms = []
room_level = []
for _ in range(p):
    l, n = sys.stdin.readline().split()
    l = int(l)
    flag = True
    for i, v in enumerate(room_level):
        if v - 10 <= l <= v + 10:
            if len(rooms[i]) < m:
                flag = False
                rooms[i].append((l, n))
                break
                 
    if flag:
        room_level.append(l)
        rooms.append([(l, n)])
        
for i in rooms:
    if len(i) == m:
        print("Started!")
    else:
        print("Waiting!")
        
    i.sort(key = lambda x: x[1])
    for j in i:
        print(j[0], j[1])
