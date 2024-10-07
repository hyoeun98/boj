import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
length = 0
for _ in range(n):
    word = sys.stdin.readline().strip()
    arr.append(word)
    length += len(word)

answer = [arr[0]]
under_score = (m - length) // (n - 1)
cnt = (m - length) - (under_score * (n - 1))

for i, v in enumerate(arr):
    if i == 0: continue
    if cnt > 0 and cnt >= (n - i):
        answer.append("_" * (under_score + 1))
        cnt -= 1
    elif v[0].isupper():
        answer.append("_" * under_score)
    elif v[0].islower():
        if cnt > 0:
            answer.append("_" * (under_score + 1))
            cnt -= 1
        else:
            answer.append("_" * under_score)
    answer.append(v)
print("".join(answer))
