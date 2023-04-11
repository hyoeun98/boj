def solution(my_string):
    my_list = my_string.split()
    my_number = [int(i) for i in my_list if i.isdigit()]
    my_op = [i for i in my_list if not i.isdigit()]
    answer = int(my_number[0])
    del my_number[0]
    for i in my_op:
        if i == "+":
            answer = answer + my_number[0]
        else:
            answer = answer - my_number[0]
        del my_number[0]
        
    return answer