import math
def solution(balls, share):
    share = min (share, balls - share)
    answer = math.factorial(balls) / (math.factorial(balls - share) * math.factorial(share))
    return answer