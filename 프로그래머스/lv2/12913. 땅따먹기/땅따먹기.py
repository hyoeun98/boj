def solution(land):
    for i, v in enumerate(land[1:]):
        for j in range(len(v)):
            land[i+1][j] += max([land[i][k] for k in range(len(land[i])) if k != j])
            
    return max(land[-1])