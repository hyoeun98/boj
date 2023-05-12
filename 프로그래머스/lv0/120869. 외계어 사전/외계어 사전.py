def solution(spell, dic):
    dic = [i for i in dic if len(i) == len(spell)]
    for d in dic:
        use = 0
        for s in spell:
            if d.count(s) == 1:
                use += 1
            else:
                break
        if use == len(spell):
            return 1
    return 2