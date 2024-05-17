# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    answer = 0

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sumQueue1 = sum(queue1)
    sumQueue2 = sum(queue2)
    maxVal = max(max(queue1), max(queue2))

    limit = len(queue1) * 3

    if (sumQueue1 + sumQueue2) % 2 != 0 or maxVal > (sumQueue1 + sumQueue2 - maxVal):
        return -1

    while sumQueue1 != sumQueue2:
        if  sumQueue1 > sumQueue2:
            val = queue1.popleft()
            queue2.append(val)
            sumQueue1 -= val
            sumQueue2 += val
        else:
            val = queue2.popleft()
            queue1.append(val)
            sumQueue2 -= val
            sumQueue1 += val

        if answer == limit:
            return -1

        answer += 1

    return answer

# result = solution([3, 2, 7, 2], [4, 6, 5, 1])
# result = solution([1, 2, 1, 2], [1, 10, 1, 2])
# result = solution([1, 1], [1, 5])
result = solution([1, 4], [4, 8])
print("result", result)
