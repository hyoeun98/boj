import sys
def check_good_seq(seq, N):
    for i in range(1, N // 2 + 1):
        for j in range(N - i):
            if seq[j: j + i] == seq[i + j: i + j + i]:
                return False # 나쁜 수열
            
    return True # 좋은 수열
  
def back_tracking(num, N):
    if len(num) == N:
        print(num)
        exit()
        
    for i in "123":
        if check_good_seq(num + i, len(num) + 1):
            back_tracking(num + i, N)
            
def solution():
    N = int(sys.stdin.readline())
    back_tracking("1", N)
        
solution()
        
