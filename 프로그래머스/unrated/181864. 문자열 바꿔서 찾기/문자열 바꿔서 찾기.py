def solution(myString, pat):
    ab_dict = {"A" : "B", "B" : "A"}
    temp = "".join([ab_dict[i] for i in myString])
            
    return 1 if pat in temp else 0