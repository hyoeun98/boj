N = int(input())
demon_num = [str(i) for i in range(666, 10000000) if '666' in str(i)][:10000]
print(demon_num[N-1])