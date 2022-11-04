def solution(n):
    answer = []
    offset = 1
    start, end = 1, n + 1
    
    while offset != n + 1:
        one_line = [i for i in range(start, end)]
        start = end
        end += n - offset
        
        if not answer:
            for i in one_line:
                answer.append([i])
                
        elif offset % 3 == 1:
            o = offset//3
            for i, v in enumerate(answer[o*2:-o]):
                answer[o*2 + i].insert(o, one_line[i])
        
        elif offset % 3 == 2:
            o = offset//3 + 1
            answer[-o] = answer[-o][:o] + one_line + answer[-o][o:]
        else:
            o = offset // 3
            for i, v in enumerate(answer[-o-1:2*o-2:-1]):
                if o == 1:
                    answer[-o-1 - i].append(one_line[i])
                else:
                    answer[-o-1 - i].insert(-o+1, one_line[i])
            
        offset += 1  
        
    answer = [j for i in answer for j in i]
    return answer