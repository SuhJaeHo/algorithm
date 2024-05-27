# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0

    q = []
    for item in scoville:
        heapq.heappush(q, item)

    while len(q) >= 1:
        minVal = heapq.heappop(q)
        if minVal >= K:
            return answer
        elif len(q) == 0:
            return -1
        else:
            nextMinVal = heapq.heappop(q)
            heapq.heappush(q, minVal + (nextMinVal * 2))
            answer += 1

    return -1

result = solution([1, 2, 3, 9, 10, 12], 7)
print("result", result)
