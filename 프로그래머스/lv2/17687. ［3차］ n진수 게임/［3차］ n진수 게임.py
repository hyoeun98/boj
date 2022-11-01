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
    len_of_num = t * m 
    num_list = "".join((map(n_nary, range(len_of_num), [n] * len_of_num)))
    answer = num_list[p-1:len_of_num:m]
    return answer