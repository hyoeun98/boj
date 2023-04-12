N = int(input())
demon_num = []
for i in range(666, 10000000):
    if "666" in (temp:= str(i)):
        demon_num.append(temp)
        if len(demon_num) > 10000:
            break
print(demon_num[N-1])