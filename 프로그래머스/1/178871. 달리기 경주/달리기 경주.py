def solution(players, callings):
    answer = []
    player_dict = {v :i + 1 for i, v in enumerate(players)}
    
    for call in callings:
        current_rank = player_dict[call]
        player_dict[call] -= 1
        players[current_rank - 2], players[current_rank - 1] = players[current_rank - 1], players[current_rank - 2]
        player_dict[players[current_rank - 1]] += 1
    return players