def solution(cards):
    answer = 0
    first_group = []
    second_group = []
    for i in range(1, len(cards)+1):
        open_box = [i]
        while True:
            last_box = cards[open_box[-1]-1]
            if last_box in open_box:
                first_group.append(open_box)
                break
                
            open_box.append(last_box)
            
    first_max_len = max(map(len,first_group))
    first_group = [i for i in first_group if len(i) == first_max_len]
    
    for i in first_group:
        open_box = i[:]
        candidate = [c for c in cards if c not in open_box]
        for j in candidate:
            open_box.append(j)
            while True:
                last_box = cards[open_box[-1]-1]
                if last_box in open_box:
                    second_group.append(open_box)
                    open_box = i[:]
                    break
                    
                else:
                    open_box.append(last_box)
                    
    second_max_len = max(map(len,second_group)) if second_group else 0
    
    return max(0, first_max_len * (second_max_len - first_max_len))