def solution(price, money, count):
    required_money = price * (count * (count + 1) / 2 ) 
    answer = required_money - money
    return max(answer, 0)