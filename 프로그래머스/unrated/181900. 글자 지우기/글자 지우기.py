def solution(my_string, indices):
    answer = [v for i, v in enumerate(my_string) if i not in indices]
        
    return "".join(answer)