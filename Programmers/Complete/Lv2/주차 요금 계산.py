# https://school.programmers.co.kr/learn/courses/30/lessons/92341

def getTime(inTime, outTime):
    time = 0

    [inHour, inMinute] = list(map(int ,inTime.split(":")))
    [outHour, outMinute] = list(map(int, outTime.split(":")))

    time += (outHour - inHour) * 60
    if inMinute > outMinute:
        time -= inMinute - outMinute
    else:
        time += outMinute - inMinute

    return time

def solution(fees, records):
    answer = []

    carDirTimeInfo = {}
    for record in records:
        [time, num, dir]= record.split(" ")
        if carDirTimeInfo.get(num):
            carDirTimeInfo[num].append(time)
        else:
            carDirTimeInfo[num] = [time]

    carDurTimeInfo = {}
    for key, times in carDirTimeInfo.items():
        acc = 0

        # if left is 1, last dir is "in"
        if len(times) % 2 == 1:
            for i in range(0, len(times), 2):
                if i == len(times) - 1:
                    acc += getTime(times[i], "23:59")
                else:
                   acc += getTime(times[i], times[i + 1])
        else:
            for i in range(0, len(times), 2):
                acc += getTime(times[i], times[i + 1])
        carDurTimeInfo[key] = acc

    carFeeInfo = []
    for key, dur in carDurTimeInfo.items():
        [baseTime, baseFee, extraTime, extraFee] = fees
        if baseTime >= dur:
            carFeeInfo.append([key, baseFee])
        else:
            totalFee = baseFee
            totalFee += ((dur - baseTime) // extraTime) * extraFee
            if (dur - baseTime) % extraTime != 0:
                totalFee += extraFee

            carFeeInfo.append([key, totalFee])

    carFeeInfo.sort(key = lambda x: x[0])
    for feeInfo in carFeeInfo:
        answer.append(feeInfo[1])

    return answer

result = solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
print("result", result)
