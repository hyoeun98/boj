def solution(polynomial):
    answer = ''
    polynomial = polynomial.split(" + ")
    x_section, constant_section = 0, 0
    for i in polynomial:
        if 'x' in i:
            x_section += int(i[:-1]) if i != 'x' else 1
        else:
            constant_section += int(i)
            
    if x_section != 0:
        answer += str(x_section) + "x" if x_section != 1 else "x"
    if constant_section != 0:
        if x_section != 0:
            answer += " + "
        answer += str(constant_section)
        
    return answer