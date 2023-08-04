def solution(arr):
    answer = []
    length = len(arr)
    i = 0
    while i < length:
        if not answer:
            answer.append(arr[i])
        elif answer and answer[-1] == arr[i]:
            del answer[-1]
        else:
            answer.append(arr[i])
        i += 1
    return answer if answer else [-1]