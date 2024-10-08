import sys

t = int(sys.stdin.readline())
strawberry = {
    0: '0010',
    1: '0001',
    2: '0010',
    3: '0011',
    4: '0100',
    5: '0101',
    6: '0110',
    7: '0111',
    8: '1000',
    9: '1001',
    10: '1010',
    11: '1011',
    12: '1100',
    13: '1101',
    14: '1110',
    15: '1111',
    16: '1110',
    17: '1101',
    18: '1100',
    19: '1011',
    20: '1010',
    21: '1001',
    22: '1000',
    23: '0111',
    24: '0110',
    25: '0101',
    26: '0100',
    27: '0011',
}
for _ in range(t):
    num = int(sys.stdin.readline())
    num %= 28
    # num = num if num <= 15 else 30 - num
    # binary = bin(num)[2:]
    # binary = binary.zfill(4)
    binary = strawberry[num]
    answer = []
    for i in binary:
        if i =="1":
            answer.append("딸기")
        else:
            answer.append("V")
    print("".join(answer))
    
