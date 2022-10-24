def solution(triangle):
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(0 if i <= 0 or j-1 < 0  else triangle[i-1][j-1], 0 if i <= 0 or j > (len(triangle[i-1])) - 1 else triangle[i-1][j])
    return max(triangle[-1])