def solution(msg):
    index_dict = {chr(v) : i+1 for i, v in enumerate(range(65, 91))}
    answer = []
    start_idx, end_idx = 0, 1
    while end_idx <= len(msg):
        if msg[start_idx : end_idx] in index_dict.keys():
            end_idx += 1
            continue
        answer.append(index_dict[msg[start_idx : end_idx - 1]])
        index_dict[msg[start_idx : end_idx]] = len(index_dict) + 1
        start_idx = end_idx - 1
        end_idx = start_idx + 1
    answer.append(index_dict[msg[start_idx : end_idx - 1]])               
        
    return answer