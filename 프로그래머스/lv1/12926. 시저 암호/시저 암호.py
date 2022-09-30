import itertools as it
def solution(s, n):
    lower = it.cycle(range(65, 91))
    upper = it.cycle(range(97, 123))
    answer = []
    for i in s:
        if i.isupper():
            answer.append((chr(ord(i) + n) if ord(i) + n <= 90 else chr(ord(i) + n-26)))
        elif i.islower():
            answer.append((chr(ord(i) + n) if ord(i) + n <= 122 else chr(ord(i) + n-26)))
        else:
            answer.append(' ')
    return "".join(answer)