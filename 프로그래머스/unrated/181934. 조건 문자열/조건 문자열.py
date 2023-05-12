def solution(ineq, eq, n, m):
    eq_dict = {">=" : lambda a, b : a >= b,
               "<=" : lambda a, b : a <= b,
               ">!" : lambda a, b : a > b,
               "<!" : lambda a, b : a < b}
    return 1 if eq_dict[ineq+eq](n, m) else 0