# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0

    people.sort()

    start = 0
    end = len(people) - 1

    while end >= start:
        left = limit - people[end]
        if left >= people[start]:
            start += 1
        # while left > 0 and left >= people[start]:
        #     left -= people[start]
        #     start += 1
        end -= 1
        answer += 1

    return answer

result = solution([70, 50, 80, 50], 100)
# result = solution([70, 80, 50], 100)
# result = solution([70, 20, 20, 30, 70, 50, 80], 100)
print("result", result)
