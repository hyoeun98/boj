def calculate(operator, a, b):
    a = int(a)
    b = int(b)
    if operator == "*":
        return a * b
    elif operator == "+":
        return a + b
    else:
        return a - b
def solution(binomial):
    a, operator, b = binomial.split()
    return calculate(operator, a, b)