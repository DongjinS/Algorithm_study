from collections import defaultdict
from math import ceil
def solution(fees, records):
    answer = []
    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee =  fees[3]
    
    cars = defaultdict(list)


    for record in records:
        div_record = record.split(' ')
        times = div_record[0].split(':')
        time = int(times[0])*60 + int(times[1])
        if div_record[2] == 'IN':
            if cars[div_record[1]]:
                cars[div_record[1]][0] = time
            else:
                cars[div_record[1]] = [-1,0]
                cars[div_record[1]][0] = time
        else:
            accum_time = time - cars[div_record[1]][0]
            cars[div_record[1]][0] = -1
            cars[div_record[1]][1] += accum_time

    for car in cars:
        lasttime = 23 * 60 + 59
        if cars[car][0] != -1:
            accum_time = lasttime - cars[car][0]
            cars[car][0] = 0
            cars[car][1] += accum_time
            
        real_time = cars[car][1]-default_time
        if real_time<0:
            real_time = 0;
        cars[car].append(default_fee + int(ceil((real_time) / unit_time)) * unit_fee)
        
    car_nums = list(cars.keys())
    car_nums.sort()
    for car in car_nums:
          answer.append(cars[car][2])

    return answer