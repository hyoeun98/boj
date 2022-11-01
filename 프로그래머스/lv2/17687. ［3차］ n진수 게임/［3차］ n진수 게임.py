def n_nary(num, n):
    t = ""
    q, r = divmod(num, n)
    t += str(r if r < 10 else chr(r+55))
    while q:
        q, r = divmod(q, n)
        t += str(r if r < 10 else chr(r+55))
    return t[::-1]

def solution(n, t, m, p):
    answer = ''
    end_of_num = 0
    a = t * m
    offset = 1
    while a > 0:
        if a >= n ** offset:
            a -= n ** offset
            end_of_num += n ** offset
        else:
            end_of_num += a // offset + 1
            break
        offset += 1

    num_list = "".join((map(n_nary, range(end_of_num), [n] * end_of_num)))
    answer = num_list[p-1::m][:t]
    return answer