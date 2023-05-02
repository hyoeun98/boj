def solution(numbers):
    answer = -999999999
    for a_idx, a in enumerate(numbers):
        for b_idx, b in enumerate(numbers[a_idx + 1:]):
            if (mul_result := a * b) > answer:
                answer = mul_result
    return answer