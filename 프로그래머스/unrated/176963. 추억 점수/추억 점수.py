from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    score_dict = defaultdict(int)
    score_dict.update(zip(name, yearning))
    for p in photo:
        photo_score = 0
        for person in p:
            photo_score += score_dict[person]
        answer.append(photo_score)
    return answer