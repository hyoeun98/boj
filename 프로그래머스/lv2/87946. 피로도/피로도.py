import itertools as it
def solution(k, dungeons):
    answer = 0
    for i in it.permutations(dungeons,len(dungeons)):
        temp_answer = 0
        temp_k = k
        for j in i:
            if j[0] <= temp_k:
                temp_answer += 1
                temp_k -= j[1]
        print(temp_answer)
        answer = max(answer, temp_answer)
        
    return answer