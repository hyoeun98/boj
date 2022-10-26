def solution(phone_book):
    phone_book = tuple(sorted(phone_book))
    for i, v in enumerate(phone_book[1:]):
        if v.startswith(phone_book[i]):
            return False
        
    return True