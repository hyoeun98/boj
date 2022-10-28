from collections import defaultdict
from datetime import timedelta
import math
def solution(fees, records):
    answer = []
    parking_dict = defaultdict(lambda : timedelta(days = 1))
    
    for i in records:
        parking_time, car_num, _ = i.split()
        parking_time = list(map(int, parking_time.split(":")))
        parking_time = timedelta(hours = parking_time[0], minutes = parking_time[1])
        if i.endswith("IN"):
            parking_dict[car_num] += parking_time
        else:
            parking_dict[car_num] -= parking_time
            
    for i in sorted(parking_dict.keys()):
        if parking_dict[i] >= timedelta(days = 1):
            parking_dict[i] = timedelta(days = 1, hours = 23, minutes = 59) - parking_dict[i]
        else:            
            parking_dict[i] = timedelta(days = 1) - parking_dict[i]
        parking_minutes = str(parking_dict[i]).split(":")
        answer.append(int(parking_minutes[0]) * 60 + int(parking_minutes[1]))
    
    for i in range(len(answer)):
        answer[i] = fees[1] + max(0, math.ceil((answer[i] - fees[0]) / fees[2]) * fees[3])
    return answer