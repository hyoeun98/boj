def solution(survey, choices):
    answer = ''
    '''
    RT
    CF
    JM
    AN
    '''
    result_dict = {'RT' : 0, 'CF' : 0, 'JM' : 0, 'AN' : 0}
    score_dict = {1 : -3, 2 : -2, 3 : -1, 4 : 0, 5 : 1, 6 : 2, 7 : 3}
    for i in range(len(survey)):
        if survey[i] in result_dict.keys():
            result_dict[survey[i]] += score_dict[choices[i]]
        else:
            result_dict[survey[i][::-1]] += score_dict[8 - choices[i]] 
            
    for i in result_dict.keys():
        if result_dict[i] <= 0:
            answer += i[0]
        else:
            answer += i[1]
    return answer