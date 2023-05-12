def solution(arr):
    answer = 0
    while True:
        temp_arr = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                i = i // 2
            elif i < 50 and i % 2 == 1:
                i = i * 2 + 1
            temp_arr.append(i)
        if arr == temp_arr:
            break
        answer += 1

        arr = temp_arr
    return answer