S = input()
alphabet = [-1] * 26
for i in range(len(S)):
    if alphabet[ord(S[i])-97] == -1:
        alphabet[ord(S[i])-97] = i
        
for i in alphabet:
    print(i, end=' ')
    