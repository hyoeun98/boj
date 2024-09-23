import sys

def solve(h, w):
    area = h * h + w * w
    answer = 150 * 150 + 1
    candidate = []
    for i in range(1, 151):
        for j in range(i + 1, 151):
            temp = i ** 2 + j ** 2
            if temp < area or (i == h and j == w):
                continue
            
            if not candidate: # 처음 만날 때
                if temp == area:
                    if i > h:
                        candidate = (i, j)
                        answer = temp
                else:
                    answer = temp
                    candidate = (i, j)
            
            elif candidate and temp <= answer:
                if temp == area and i < h:
                    continue
                if temp == answer:
                    if i < candidate[0]:
                        candidate = (i, j)
                elif temp < answer:
                    answer = temp
                    candidate = (i, j)

    print(*candidate)
                
    
while True:
    h, w = map(int, sys.stdin.readline().split())
    if h == 0 and w == 0:
        break
    
    solve(h, w)