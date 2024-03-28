import sys    

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    mbti = sys.stdin.readline().split()
    if n > 32:
        print(0)

    else:
        cnt = 999
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    temp = sum([0 if mbti[i][idx] == mbti[j][idx] else 1 for idx in range(4)])
                    temp += sum([0 if mbti[i][idx] == mbti[k][idx] else 1 for idx in range(4)])
                    temp += sum([0 if mbti[j][idx] == mbti[k][idx] else 1 for idx in range(4)])
                    cnt = min(cnt, temp)
                    
        print(cnt)
            