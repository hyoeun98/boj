import re
def solution(files):
    answer = []
    for f_idx, f in enumerate(files):
        head_idx = re.search("[0-9]", f).span()[0]
        num_idx = re.search("[0-9]{1,5}", f[head_idx:]).span()[1]

        head = f[:head_idx].lower()
        num = int(f[head_idx:head_idx + num_idx])
        answer.append([head, num, f_idx])

    answer.sort(key = lambda x : (x[0].lower(), x[1]))
    
    return [files[i[2]] for i in answer]