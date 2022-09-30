def solution(n, arr1, arr2):
    bin_arr1 = [str(bin(i))[2:].zfill(n) for i in arr1]
    bin_arr2 = [str(bin(i))[2:].zfill(n) for i in arr2]
    
    answer = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            answer[i][j] = "#" if int(bin_arr1[i][j]) or int(bin_arr2[i][j]) else " "
    return list(map("".join, answer))