def solution(n):
    binary_n = bin(n)
    for i in range(n + 1, n * 2):
        if bin(i).count('1') == binary_n.count('1'):
            return i
