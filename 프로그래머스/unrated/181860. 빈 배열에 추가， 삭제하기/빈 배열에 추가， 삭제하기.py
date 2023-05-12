def solution(arr, flag):
    answer = []
    for i, v in enumerate(flag):
        if v:
            answer.extend([arr[i]] * arr[i] * 2)
        else:
            for _ in range(arr[i]):
                del answer[-1]
    return answer