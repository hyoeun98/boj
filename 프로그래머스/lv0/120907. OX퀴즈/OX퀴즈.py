def operation(first, second, operator):
    if operator == "+":
        return first + second
    else:
        return first - second
    
def solution(quiz):
    answer = []
    for i in quiz:
        problem = i.split()
        first = int(problem[0])
        second = int(problem[2])
        operator = problem[1]
        result = int(problem[-1])
        if operation(first, second, operator) == result:
            answer.append("O")
        else:
            answer.append("X")
    return answer