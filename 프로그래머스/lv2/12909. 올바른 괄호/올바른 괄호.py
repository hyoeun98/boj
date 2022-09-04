def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            try:
                del stack[-1]
            except:
                return False
    
    return False if len(stack) > 0 else True