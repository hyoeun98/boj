import fractions
def solution(numer1, denom1, numer2, denom2):
    a = fractions.Fraction(numer1, denom1)
    b = fractions.Fraction(numer2, denom2)
    c = a+b
    return [c.numerator, c.denominator]