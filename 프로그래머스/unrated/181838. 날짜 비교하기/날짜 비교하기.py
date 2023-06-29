def solution(date1, date2):
    answer = 0
    f_year, f_month, f_day = map(int ,date1)
    s_year, s_month, s_day = map(int ,date2)
    if f_year < s_year:
        return 1
    elif f_year > s_year:
        return 0
    
    if f_month < s_month:
        return 1
    elif f_month > s_month:
        return 0
    
    if f_day < s_day:
        return 1
    elif f_day < s_day:
        return 0
    return 0