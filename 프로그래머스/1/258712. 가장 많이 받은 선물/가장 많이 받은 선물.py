# 선물을 가장 많이 받을 친구가 받을 선물의 수
def solution(friends, gifts):
    answer = 0
    board = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    friend_dict = {v : i for i, v in enumerate(friends)}
    
    for i in gifts:
        a, b = i.split()
        a, b = friend_dict[a], friend_dict[b]
        board[a][b] += 1
    
    for send_idx, i in enumerate(board):
        num_gift = 0
        for get_idx, j in enumerate(i):
            if get_idx != send_idx and j > board[get_idx][send_idx]:
                num_gift += 1
            elif j == board[get_idx][send_idx]:
                if sum(i) - sum([b[send_idx] for b in board]) > sum(board[get_idx]) - sum([b[get_idx] for b in board]):
                    num_gift += 1
                
        answer = max(answer, num_gift)
    print(board)
    
    return answer