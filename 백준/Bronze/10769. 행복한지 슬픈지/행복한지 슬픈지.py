import sys

string = sys.stdin.readline().strip()
happy_cnt = string.count(":-)")
sad_cnt = string.count(":-(")

if happy_cnt > sad_cnt:
    print("happy")
elif sad_cnt > happy_cnt:
    print("sad")
elif sad_cnt == happy_cnt:
    if sad_cnt == 0:
        print("none")
    else:
        print("unsure")