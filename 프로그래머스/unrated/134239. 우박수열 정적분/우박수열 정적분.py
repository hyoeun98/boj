import itertools as it
def solution(k, ranges):
    answer = []
    collatz_list = []
    collatz = k
    while collatz != 1:
        collatz_list.append(collatz)
        if collatz % 2 == 0:
            collatz //= 2
        else:
            collatz *= 3
            collatz += 1
    collatz_list.append(1)
    
    dp_list = []
    for i in range(len(collatz_list) - 1):
        a = collatz_list[i]
        b = collatz_list[i+1]
        dp_list.append((a+b) / 2)

    dp_list = [0] + list(it.accumulate(dp_list))
    dp_len = len(dp_list)
    for i in ranges:
        if i[0] >= dp_len or dp_len < -i[1] or i[0] - i[1] >= dp_len:
            answer.append(-1.0)
        else:
            answer.append(dp_list[i[1]-1] - dp_list[i[0]])

    return answer