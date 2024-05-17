# https://school.programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    answer = 0
    maxStone = max(stones)

    left = 0
    right = maxStone

    while right >= left:
        mid = (left + right) // 2

        flag = True
        gap = 0
        for i in range(len(stones)):
            if mid > stones[i]:
                gap += 1
            else:
                gap = 0

            if gap >= k:
                flag = False
                break

        if flag:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

result = solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
print("result", result)
