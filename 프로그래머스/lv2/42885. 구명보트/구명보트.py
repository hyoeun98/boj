def solution(people, limit):
    answer, weight = 0, 0
    people.sort(reverse = True)

    for i in people:
        weight = i
        
        for j in range(-1, -6, -1):
            weight += people[j]
            if weight > limit:
                answer += 1
                break
                          
            else:
                del people[j]
                
    return answer