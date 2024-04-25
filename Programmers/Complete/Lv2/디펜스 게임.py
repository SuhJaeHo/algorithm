# https://school.programmers.co.kr/learn/courses/30/lessons/142085

import heapq

def solution(n, k, enemy):
    answer = 0

    heap = []
    acc = 0

    while acc <= n and answer != len(enemy):
        acc += enemy[answer]
        heapq.heappush(heap, -enemy[answer])

        if acc > n:
            if k > 0:
                acc += heapq.heappop(heap)
                k -= 1
            else:
                break

        answer += 1

    return answer

# result = solution(7, 3, [4, 2, 4, 5, 3, 3, 1])
result = solution(7, 3, [2, 2, 4, 5, 2, 3, 1])
print("result", result)
