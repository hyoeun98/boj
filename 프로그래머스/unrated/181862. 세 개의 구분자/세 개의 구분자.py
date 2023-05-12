import re
def solution(myStr):
    myStr = re.split('[abc]', myStr)
    myStr = [i for i in myStr if i != ""]
    return myStr if myStr else ["EMPTY"]