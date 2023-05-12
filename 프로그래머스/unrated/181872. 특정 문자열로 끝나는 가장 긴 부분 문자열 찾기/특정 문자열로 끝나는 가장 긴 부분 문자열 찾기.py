def solution(myString, pat):
    while not myString.endswith(pat):
        myString = myString[:-1]
    return myString