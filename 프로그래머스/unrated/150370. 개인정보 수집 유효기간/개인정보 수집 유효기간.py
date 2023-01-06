def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split(".")))
    term_dict = dict()
    for i in terms:
        kind, period = i.split()
        term_dict[kind] = int(period)
    
    for i in privacies:
        date, kind = i.split()
        year, month, day = list(map(int, date.split(".")))
        month = month + term_dict[kind]
        if month > 12:
            div, mod = divmod(month, 12)
            if mod == 0:
                month = 12
                year += div-1
            else:
                month = mod
                year += div
            
        answer.append([year, month, day])
        
    return [i+1 for i, v in enumerate(answer) if today >= v]