# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def my_solution(progresses, speeds):
    answer = []
    days = []

    for i in range(len(progresses)):
        left = 100 - progresses[i]
        if left % speeds[i] != 0:
            days.append((left // speeds[i]) + 1)
        else:
            days.append((left // speeds[i]))

    cnt = 1
    curr = days[0]
    for i in range(1, len(days)):
        if curr >= days[i]:
            cnt += 1
        else:
            answer.append(cnt)
            curr = days[i]
            cnt = 1

        if i == (len(days) - 1):
            answer.append(cnt)

    return answer

def solution(progresses, speeds):
    answer = []
    days = 0
    cnt = 0

    while len(progresses) > 0:
        if (progresses[0] + days * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            else:
                days += 1

    answer.append(cnt)
    return answer

# result = solution([93, 30, 55], [1, 30, 5])
result = solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
print("result", result)
