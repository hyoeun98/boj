import re
def solution(myString):
    myString = re.sub("x+", "x", myString)
    myString = myString.strip("x")
    myString = myString.split("x")
    myString.sort()
    return myString