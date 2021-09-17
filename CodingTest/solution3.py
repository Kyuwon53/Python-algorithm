import math
def solution(fees, records):
    answer = []
    # 요금
    primaryTime = fees[0]   #기본시간
    primaryFee = fees[1]    # 기본요금
    UnitTime = fees[2]      # 단위시간
    UnitFee = fees[3]       # 단위요금

    # 차량번호
    car_num = set()
    for rec in records:
        car_num.add(rec.split()[1])
    car_num = sorted(car_num)
    # 주차 시간 저장
    parking_time = [0 for i in range(len(car_num))]
    # 입출력 기록
    in_out_rec = [0 for i in range(len(car_num))]
    # 시간 변환 함수
    def time_transfer(x) :
        hour = int(x.split(':')[0])
        minute = int(x.split(':')[1])
        return hour * 60 + minute

    # 누적 주차 시간
    for rec in records:
        for car in car_num:
            if rec.split()[1] == car:
                idx = car_num.index(car)  # 해당 차량번호 위치
                in_out_rec[idx] = rec.split()[2]    # 해당 차량번호 입출상태
                if in_out_rec[idx] == 'IN':
                    parking_time[idx] -= time_transfer(rec.split()[0])
                if in_out_rec[idx] == 'OUT':
                    parking_time[idx] += time_transfer(rec.split()[0])

    # 마지막 출차가 없는 경우 출차 시간 23:59분
    for car in car_num:
        if in_out_rec[car_num.index(car)] == 'IN':
            parking_time[car_num.index(car)] += time_transfer('23:59')

    # 주차요금 계산
    for time in parking_time:
        if time <= primaryTime:
            answer.append(primaryFee)
        if time > primaryTime:
            fee = primaryFee + math.ceil((time - primaryTime) / UnitTime) * UnitFee
            answer.append(fee)
    return answer


fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))
