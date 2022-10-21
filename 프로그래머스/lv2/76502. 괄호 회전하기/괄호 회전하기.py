from collections import deque
def solution(s):
    answer = 0
    s = deque(s)
    brackets = {')' : '(', '}' : '{', ']' : '['}
    open_brackets = ['(', '{', '[']
    for _ in range(len(s)):
        s.rotate(-1)
        stack = []
        for i in s:
            if i in open_brackets:
                stack.append(i)
            else:
                if not stack:
                    answer -= 1
                    break
                elif brackets[i] == stack[-1]:
                    del stack[-1]
                    pass
                else:
                    break
        
        if not stack:
            answer += 1

    return answer