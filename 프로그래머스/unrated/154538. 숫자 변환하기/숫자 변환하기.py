from collections import deque
def bfs(calc_list, x, y):
    queue = deque([x])
    cnt = [0] * (y+1)
    while queue:
        node = queue.popleft()
        for func in calc_list:
            if (temp:= func(node)) <= y and cnt[temp] == 0:
                queue.append(temp)
                cnt[temp] = cnt[node] + 1
                if temp == y:
                    return cnt[temp]
                
    return -1
    
def solution(x, y, n):
    if x == y:
        return 0
    calc_list = [lambda x: x + n, lambda x: x * 2, lambda x: x * 3]
        
    return bfs(calc_list, x, y)