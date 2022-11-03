import copy
answer = [0, 0]

def dc(matrix, offset):
    if offset >= 1:
        t1, t2, t3, t4 = divide(matrix, offset)
        for i in [t1, t2, t3, t4]:
            if not conquer(i):
                dc(i, offset // 2)
    
def conquer(matrix):
    t = set([j for i in matrix for j in i])
    if len(t) == 1:
        global answer
        answer[t.pop()] += 1
        return True
    else:
        return False
    
def divide(matrix, offset):
    t = copy.deepcopy(matrix)
    t1 = t[:offset]
    t2 = t[offset:]
    t11 = list(zip(*t1))[:offset]
    t12 = list(zip(*t1))[offset:]
    t21 = list(zip(*t2))[:offset]
    t22 = list(zip(*t2))[offset:]
    return t11, t12, t21, t22
    
def solution(arr):
    if not conquer(arr):
        dc(arr, len(arr)//2)
    return answer