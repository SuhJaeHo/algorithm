# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0

    left = 1
    right = max(times) * n

    while right >= left:
        mid = (left + right) // 2

        cnt = 0
        for time in times:
            cnt += (mid // time)

        if cnt >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

result = solution(6, [7, 10])
print("result", result)
