import itertools as it
def solution(users, emoticons):
    answer = [0, 0]
    sale_dict = {40 : 3, 30 : 2, 20 : 1, 10: 0}
    
    for i, v in enumerate(users):
        if v[0] % 10 != 0:
            users[i][0] = v[0] + 10 - v[0] % 10

    saled_emoticons = []
    for i in emoticons:
        saled_emoticons.append([int(i*j*0.1) for j in range(9, 5, -1)])
    
    idx = [list(range(4))] * len(emoticons)
    for i in list(it.product(*idx)):
        prices = []
        for j, v in enumerate(i):
            prices.append(saled_emoticons[j][v])
        
        sub = 0
        profit = 0
        for user in users:
            buy = 0
            t = sale_dict[user[0]]
            for index, p in enumerate(i):
                if t <= p:
                    buy += prices[index]
            if buy >= user[1]:
                sub += 1
            else:
                profit += buy
        answer = max(answer, [sub, profit])    
        
    return answer