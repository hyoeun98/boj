def solution(arrayA, arrayB):
    answer = 0
    candidateA = []
    for i in range(2, arrayA[0] // 2 + 1):
        if arrayA[0] % i == 0:
            candidateA.append(i)
    candidateA.append(arrayA[0])
    
    for i in candidateA[:]:
        for j in arrayA:
            if j % i != 0:
                candidateA.remove(i)
                break
                
    for i in candidateA[::-1]:
        is_require = True
        
        for j in arrayB:
            if j % i == 0:
                is_require = False 
                break
        if is_require:
            answer = i
            break
    
    candidateB = []
    for i in range(2, arrayB[0] // 2 + 1):
        if arrayB[0] % i == 0:
            candidateB.append(i)
    candidateB.append(arrayB[0])
    
    for i in candidateB[:]:
        for j in arrayB[1:]:
            if j % i != 0:
                candidateB.remove(i)
                break
                
    for i in candidateB[::-1]:
        is_require = True
        
        for j in arrayA:
            if j % i == 0:
                is_require = False 
                break
        if is_require:
            answer = max(answer, i)
            break
        
    return answer