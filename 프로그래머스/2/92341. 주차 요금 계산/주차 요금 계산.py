import math

def time_cal(number, new_record):
    number_record = [i for i in new_record if i[1] == number]
    if len(number_record) % 2 != 0:
        number_record.append(["23:59",number, "OUT"])
        
    time_lst = []
    for time in range(1, len(number_record),2):
        in_hour = int(number_record[time -1][0][:2])
        in_mins = int(number_record[time -1][0][-2:])
        out_hour = int(number_record[time][0][:2])
        out_mins = int(number_record[time][0][-2:])
        
        hour_taken = (out_hour - in_hour) * 60
        min_taken = out_mins - in_mins
        total_taken = hour_taken + min_taken
        time_lst.append(total_taken)
    return sum(time_lst)

def solution(fees, records):
    new_record = [i.split(" ") for i in records]
    car_number = sorted(list(set([i[1] for i in new_record])))
    paid = []
    for num in car_number:
        total_time = time_cal(num, new_record)
        
        if total_time <= fees[0]:
            paid.append(fees[1])
        else:
            extra_time = total_time - fees[0]
            extra_units = math.ceil(extra_time / fees[2])
            money = fees[1] + (extra_units * fees[3])
            paid.append(money)
            
        
    return paid