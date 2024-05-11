# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    answer = 0

    queue = deque([(priorities[i], i) for i in range(len(priorities))])

    while queue:
        max = 0
        for i in range(len(queue)):
            if queue[i][0] > max:
                max = queue[i][0]

        val, idx = queue.popleft()

        if val != max:
            queue.append((val, idx))
        else:
            answer += 1
            if idx == location:
                return answer

    return answer

result = solution([2, 1, 3, 2], 2)
# result = solution([1, 1, 9, 1, 1, 1], 0)
print("result", result)
