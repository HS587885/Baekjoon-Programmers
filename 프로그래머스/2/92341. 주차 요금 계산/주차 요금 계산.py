# import math

# def time_cal(number, new_record):
#     number_record = [i for i in new_record if i[1] == number]
#     if len(number_record) % 2 != 0:
#         number_record.append(["23:59",number, "OUT"])
        
#     time_lst = []
#     for time in range(1, len(number_record),2):
#         in_hour = int(number_record[time -1][0][:2])
#         in_mins = int(number_record[time -1][0][-2:])
#         out_hour = int(number_record[time][0][:2])
#         out_mins = int(number_record[time][0][-2:])
        
#         hour_taken = (out_hour - in_hour) * 60
#         min_taken = out_mins - in_mins
#         total_taken = hour_taken + min_taken
#         time_lst.append(total_taken)
#     return sum(time_lst)

# def solution(fees, records):
#     new_record = [i.split(" ") for i in records]
#     car_number = sorted(list(set([i[1] for i in new_record])))
#     paid = []
#     for num in car_number:
#         total_time = time_cal(num, new_record)
        
#         if total_time <= fees[0]:
#             paid.append(fees[1])
#         else:
#             extra_time = total_time - fees[0]
#             extra_units = math.ceil(extra_time / fees[2])
#             money = fees[1] + (extra_units * fees[3])
#             paid.append(money)
            
        
#     return paid

import math
from collections import defaultdict

def solution(fees, records):
    car_times = defaultdict(int)  # 차량별 총 시간 저장
    last_seen = {}  # 차량별 마지막 입차 시간 기록

    for record in records:
        time, number, action = record.split()
        hour, minute = map(int, time.split(':'))
        minutes_since_midnight = hour * 60 + minute  # 시간 → 분 단위로 변환

        if action == "IN":
            last_seen[number] = minutes_since_midnight
        elif action == "OUT":
            in_time = last_seen.pop(number)
            car_times[number] += minutes_since_midnight - in_time

    # 입차 기록이 남아 있는 차량은 23:59에 출차된 것으로 처리
    for number, in_time in last_seen.items():
        car_times[number] += (23 * 60 + 59) - in_time

    # 차량 번호 순서대로 요금 계산
    result = []
    for number in sorted(car_times):
        total_time = car_times[number]
        if total_time <= fees[0]:
            result.append(fees[1])
        else:
            extra_time = total_time - fees[0]
            extra_units = math.ceil(extra_time / fees[2])
            money = fees[1] + (extra_units * fees[3])
            result.append(money)

    return result
