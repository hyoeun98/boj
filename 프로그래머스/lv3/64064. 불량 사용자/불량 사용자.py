import itertools as it
import re

def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        ban_pattern = re.compile(re.sub("\*", ".", banned_id[i]))
        if not ban_pattern.match(users[i]):
            return False
    return True
        

def solution(user_id, banned_id):
    user_permutation = list(it.permutations(user_id, len(banned_id)))
    answer = []
    for i in user_permutation:
        if not check(i, banned_id):
            continue
        else:
            users = set(i)
            if users not in answer:
                answer.append(users)

            
    return len(answer)