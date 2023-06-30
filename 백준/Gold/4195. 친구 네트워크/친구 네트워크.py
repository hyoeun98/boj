import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    else:
        return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
        friend_cnt[a] += friend_cnt[b]
        friend_cnt[b] = friend_cnt[a]
    else:
        parent[a] = b
        friend_cnt[b] += friend_cnt[a]
        friend_cnt[a] = friend_cnt[b]

n = int(sys.stdin.readline())
for _ in range(n):
    F = int(sys.stdin.readline())
    parent = [i for i in range(F * 2)]
    friend_cnt = [0 for _ in range(F * 2)]
    names = dict()
    name_to_num_cnt = 0
    
    for _ in range(F):
        a, b = sys.stdin.readline().split()

        if a in names:
            a = names[a]
        else:
            names[a] = name_to_num_cnt
            a = name_to_num_cnt
            name_to_num_cnt += 1
            friend_cnt[a] += 1

        if b in names:
            b = names[b]
        else:
            names[b] = name_to_num_cnt
            b = name_to_num_cnt
            name_to_num_cnt += 1
            friend_cnt[b] += 1

        parent_a = find(a)
        parent_b = find(b)

        if parent_a == parent_b:
            print(friend_cnt[parent_a])
        else:
            print(friend_cnt[parent_a] + friend_cnt[parent_b])
            union(a, b)

