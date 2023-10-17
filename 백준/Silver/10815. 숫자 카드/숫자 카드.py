import sys
import bisect
def solution():
    n = int(sys.stdin.readline())
    card = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    candidate = list(map(int, sys.stdin.readline().split()))
    card_dict = dict()
    for i in card:
        card_dict[i] = 1
    
    for i in candidate:
        if i in card_dict:
            print(1, end = " ")
        else:
            print(0, end = " ")

solution()

